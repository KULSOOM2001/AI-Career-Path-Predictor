# 🤖 AI Career Path Predictor

**95% Accuracy | Decision Tree | Flask Web App | Dark/Light Theme**

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-black)
![Accuracy](https://img.shields.io/badge/Accuracy-95%25-brightgreen)

---

## Overview

AI Career Path Predictor recommends tech career paths based on student skills using Machine Learning.

### Input Features

- Favourite Subject (Mathematics, Programming, Science, Design, Networking, Business)
- Coding Interest (Low/Medium/High)
- Math Skill (Low/Medium/High)
- Creativity Level (Low/Medium/High)
- Communication Skill (Low/Medium/High)
- Problem Solving Skill (Low/Medium/High)

### Career Paths

1. Artificial Intelligence 🤖
2. Cybersecurity 🔒
3. Data Science 📊
4. Software Engineering 💻
5. Web Development 🌐

---

## Features

- ✅ ML Predictions with 95% Accuracy
- ✅ Feature Importance Visualization
- ✅ Confidence Scores with Progress Bar
- ✅ Dark/Light Theme Toggle
- ✅ Smooth CSS Animations
- ✅ Fully Responsive Design
- ✅ Real-time Predictions

---

## System Architecture

```
User Browser (index.html)
        │
        ▼
Flask Backend (app.py)
        │
        ▼
ML Model (model.pkl - Decision Tree)
        │
        ▼
Result Page (result.html)
```

**Data Flow:** User Input → HTTP POST → Flask → ML Model → Prediction → Result Page

---

## Model Performance

### Classification Report

| Career Path | Precision | Recall | F1-Score |
|-------------|-----------|--------|----------|
| Artificial Intelligence | 84% | 73% | 78% |
| Cybersecurity | 89% | 90% | 89% |
| Data Science | 83% | 91% | 87% |
| Software Engineering | 87% | 91% | 89% |
| Web Development | 85% | 85% | 85% |

### Overall Accuracy

**95.0%**

### Model Comparison

- Decision Tree: 95.0% (Best)
- KNN: 81.1%

---

## Technologies Used

| Category | Technology |
|----------|------------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Frontend | HTML5, CSS3, JavaScript |

---

## Project Structure

```
AI-Career-Path-Predictor/
├── app.py
├── data/
│   └── career_dataset.csv
├── model/
│   ├── train_model.py
│   └── model.pkl
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

---

## Installation

```bash
git clone https://github.com/KULSOOM2001/AI-Career-Path-Predictor.git
cd AI-Career-Path-Predictor
pip install flask pandas numpy scikit-learn
cd model
python train_model.py
cd ..
python app.py
```

Open: http://127.0.0.1:5000

---

## Usage

1. Fill the skill assessment form
2. Click "Predict My Career"
3. View your career match

---

## Feature Importance

| Feature | Importance |
|---------|------------|
| Creativity Level | 46.8% |
| Math Skill | 24.2% |
| Communication Skill | 23.6% |
| Favourite Subject | 2.3% |
| Coding Interest | 1.9% |
| Problem Solving Skill | 1.1% |

**Insight:** Creativity is the most important factor for tech career prediction!

---

⭐ Star this repository if you found it helpful!
```

Copy this exact code into `README.md` file and push again. It will render properly on GitHub.
