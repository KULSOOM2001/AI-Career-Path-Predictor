import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Load Dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "career_dataset.csv")

df = pd.read_csv(DATA_PATH)
print(f"Dataset loaded: {df.shape[0]} rows")

# Encode Features
encoders = {}
feature_cols = [
    "favourite_subject",
    "coding_interest",
    "math_skill",
    "creativity_level",
    "communication_skill",
    "problem_solving_skill"
]

for col in feature_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

target_le = LabelEncoder()
df["career_path"] = target_le.fit_transform(df["career_path"])
encoders["career_path"] = target_le

X = df[feature_cols]
y = df["career_path"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

# Decision Tree
dt = DecisionTreeClassifier(max_depth=8, min_samples_split=10, random_state=None)
dt.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test))
print(f"Decision Tree Accuracy: {dt_acc*100:.2f}%")

# KNN
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
knn_acc = accuracy_score(y_test, knn.predict(X_test))
print(f"KNN Accuracy: {knn_acc*100:.2f}%")

# Best Model Select
if dt_acc >= knn_acc:
    best_model = dt
    best_name = "Decision Tree"
    best_acc = dt_acc
else:
    best_model = knn
    best_name = "KNN"
    best_acc = knn_acc

print(f"\nBest Model: {best_name} ({best_acc*100:.2f}%)")
print(classification_report(
    y_test, best_model.predict(X_test),
    target_names=target_le.classes_
))

# Save Model
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.pkl")
save_data = {
    "model": best_model,
    "encoders": encoders,
    "feature_cols": feature_cols,
    "model_name": best_name,
    "accuracy": best_acc,
}
with open(MODEL_PATH, "wb") as f:
    pickle.dump(save_data, f)

print(f"\nModel saved!")