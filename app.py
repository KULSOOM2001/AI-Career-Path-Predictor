from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

# Career Information
CAREER_INFO = {
    "Artificial Intelligence": {
        "icon": "🤖",
        "desc": "Build intelligent systems, neural networks, and future-ready AI solutions.",
        "skills": ["Python", "Machine Learning", "Deep Learning", "Math", "Data Structures"],
        "roles": ["AI Engineer", "ML Engineer", "Research Scientist", "Computer Vision Engineer"]
    },
    "Cybersecurity": {
        "icon": "🔒",
        "desc": "Protect digital assets, prevent attacks, and secure networks.",
        "skills": ["Network Security", "Cryptography", "Risk Assessment", "Penetration Testing", "Linux"],
        "roles": ["Security Analyst", "Penetration Tester", "SOC Engineer", "Security Consultant"]
    },
    "Data Science": {
        "icon": "📊",
        "desc": "Extract insights from data, build predictive models, and drive decisions.",
        "skills": ["Statistics", "Python/R", "SQL", "Data Visualization", "Machine Learning"],
        "roles": ["Data Scientist", "Data Analyst", "BI Developer", "Analytics Engineer"]
    },
    "Software Engineering": {
        "icon": "💻",
        "desc": "Design, develop, and maintain scalable software systems.",
        "skills": ["Programming", "System Design", "Databases", "Git", "Testing"],
        "roles": ["Software Engineer", "Backend Dev", "Full Stack Dev", "System Architect"]
    },
    "Web Development": {
        "icon": "🌐",
        "desc": "Create beautiful, responsive websites and web applications.",
        "skills": ["HTML/CSS", "JavaScript", "React/Vue", "Node.js", "UI/UX"],
        "roles": ["Frontend Dev", "Backend Dev", "Full Stack Dev", "Web Designer"]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = load_model()
    model = data['model']
    encoders = data['encoders']
    feature_cols = data['feature_cols']
    model_name = data['model_name']
    accuracy = round(data['accuracy'] * 100, 2)
    
    # Get form values
    form_data = {}
    for col in feature_cols:
        val = request.form.get(col)
        form_data[col] = val
    
    # Encode input
    encoded_input = []
    for col in feature_cols:
        val = request.form.get(col)
        # Handle unseen labels
        try:
            encoded_val = encoders[col].transform([val])[0]
        except ValueError:
            # If value not seen during training, use the most common or default
            encoded_val = 1  # Default to Medium
        encoded_input.append(encoded_val)
    
    # Predict
    prediction = model.predict([encoded_input])[0]
    career = encoders['career_path'].inverse_transform([prediction])[0]
    
    # Get probabilities if available
    probs = None
    all_probs = None
    confidence = None
    
    if hasattr(model, 'predict_proba'):
        probs = model.predict_proba([encoded_input])[0]
        # Create dict of career: probability
        all_probs = {}
        for i, prob in enumerate(probs):
            career_name = encoders['career_path'].inverse_transform([i])[0]
            all_probs[career_name] = round(prob * 100, 1)
        
        # Get confidence (max probability)
        confidence = round(float(max(probs)) * 100, 1)
    
    # Get feature importance if available
    feature_importance = None
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        # Get readable feature names
        features = [f.replace('_', ' ').title() for f in feature_cols]
        feature_importance = sorted(zip(features, importances.tolist()), key=lambda x: x[1], reverse=True)
    
    return render_template('result.html',
                         career=career,
                         info=CAREER_INFO.get(career, {}),
                         inputs=form_data,
                         confidence=confidence,
                         all_probs=all_probs,
                         model_name=model_name,
                         accuracy=accuracy,
                         feature_importance=feature_importance)

if __name__ == '__main__':
    app.run(debug=True)