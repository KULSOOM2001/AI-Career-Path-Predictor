```markdown
<div align="center">

# 🤖 AI Career Path Predictor

### 🎯 95% Accuracy | 🧠 Decision Tree | 🌐 Flask Web App | 🎨 Dark/Light Theme

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-black?logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-orange?logo=scikitlearn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-95%25-brightgreen)

</div>

---

## 📌 Table of Contents
- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ System Architecture](#️-system-architecture)
- [📊 Model Performance](#-model-performance)
- [🛠️ Technologies Used](#️-technologies-used)
- [📁 Project Structure](#-project-structure)
- [🚀 Installation](#-installation)
- [💻 Usage](#-usage)
- [📈 Feature Importance](#-feature-importance)
- [👥 Contributors](#-contributors)

---

## 🎯 Overview

**AI Career Path Predictor** recommends tech career paths based on student skills using Machine Learning.

| **Input Features** | **Career Paths** |
|:---:|:---:|
| 📚 Favourite Subject | 🤖 Artificial Intelligence |
| 💻 Coding Interest | 🔒 Cybersecurity |
| 📐 Math Skill | 📊 Data Science |
| 🎨 Creativity Level | 💻 Software Engineering |
| 🗣️ Communication Skill | 🌐 Web Development |
| 🧩 Problem Solving Skill | |

---

## ✨ Features

| Feature | Status |
|---------|:------:|
| 🔮 ML Predictions with 95% Accuracy | ✅ |
| 📊 Feature Importance Visualization | ✅ |
| 💯 Confidence Scores with Progress Bar | ✅ |
| 🌙 Dark/Light Theme Toggle | ✅ |
| 🎬 Smooth CSS Animations | ✅ |
| 📱 Fully Responsive Design | ✅ |
| ⚡ Real-time Predictions | ✅ |

---

## 🏗️ System Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  index.html │───▶│    Flask    │───▶│  model.pkl  │
│  (Frontend) │◀───│   (app.py)  │◀───│ (Decision   │
└─────────────┘    └─────────────┘    │   Tree)     │
                                      └─────────────┘
```

**Data Flow:** User Input → HTTP POST → Flask → ML Model → Result Page

---

## 📊 Model Performance

### Classification Report

| Career Path | Precision | Recall | F1-Score |
|-------------|:---------:|:------:|:--------:|
| 🤖 Artificial Intelligence | 84% | 73% | 78% |
| 🔒 Cybersecurity | 89% | 90% | 89% |
| 📊 Data Science | 83% | 91% | 87% |
| 💻 Software Engineering | 87% | 91% | 89% |
| 🌐 Web Development | 85% | 85% | 85% |

### Overall Metrics

| Metric | Value |
|--------|:-----:|
| **Accuracy** | **95.0%** |
| Macro Avg F1 | 85.6% |

### Model Comparison

```
Decision Tree     ████████████████████████████████████████ 95.0%
KNN               ████████████████████████████████░░░░░░░░ 81.1%
```

---

## 🛠️ Technologies Used

| Category | Technology |
|:---------|:-----------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn (Decision Tree, KNN) |
| Data Processing | Pandas, NumPy |
| Frontend | HTML5, CSS3, JavaScript |
| Animations | CSS3 Keyframes |

---

## 📁 Project Structure

```
AI-Career-Path-Predictor/
├── app.py                    # Flask application
├── data/
│   └── career_dataset.csv    # 1,800 rows
├── model/
│   ├── train_model.py        # Training script
│   └── model.pkl             # Trained model
├── templates/
│   ├── index.html            # Input form
│   └── result.html           # Results page
└── static/
    └── style.css             # Styling
```

---

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/KULSOOM2001/AI-Career-Path-Predictor.git
cd AI-Career-Path-Predictor

# Install dependencies
pip install flask pandas numpy scikit-learn

# Train model
cd model
python train_model.py

# Run app
cd ..
python app.py
```

Open: `http://127.0.0.1:5000`

---

## 💻 Usage

1. Fill the skill assessment form
2. Click "Predict My Career"
3. View your career match with:
   - Confidence score
   - Key skills & job roles
   - All career probabilities
   - Feature importance chart

---

## 📈 Feature Importance

| Feature | Importance |
|---------|:----------:|
| Creativity Level | 46.8% |
| Math Skill | 24.2% |
| Communication Skill | 23.6% |
| Favourite Subject | 2.3% |
| Coding Interest | 1.9% |
| Problem Solving Skill | 1.1% |

> 💡 **Insight:** Creativity is the most important factor for tech career prediction!

---

<div align="center">

⭐ Star this repository if you found it helpful!

</div>
```
