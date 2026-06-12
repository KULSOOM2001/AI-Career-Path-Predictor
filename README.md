<div align="center">

# 🚀 AI Career Path Predictor

### *Intelligent Career Guidance System Powered by Machine Learning*

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-1.4-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-95%25-22C55E?style=for-the-badge)

</div>

---

## 📖 Project Overview

**AI Career Path Predictor** is an intelligent web application that leverages Machine Learning to help students discover their ideal career path in the technology sector. By analyzing six key skill parameters, the system provides data-driven career recommendations with **95% accuracy**.

### 🎯 Problem Statement

Students often struggle to choose the right career path due to information overload and lack of objective guidance. This system bridges that gap by offering personalized, data-driven career recommendations.

### 💡 Our Solution

A Flask-based web application that uses a **Decision Tree classifier** to predict the most suitable career path based on individual skill profiles.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔮 **Smart Predictions** | Machine learning-based career recommendations |
| 📊 **Feature Importance** | Visual breakdown of which skills matter most |
| 💯 **Confidence Scores** | Probability distribution across all career paths |
| 🌙 **Dark/Light Theme** | Toggle between themes with persistent preference |
| 🎬 **Smooth Animations** | Professional UI with CSS keyframe animations |
| 📱 **Responsive Design** | Seamless experience across all devices |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         THREE-TIER ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │   CLIENT     │      │   SERVER     │      │    MODEL     │   │
│  │   TIER       │ ───► │   TIER       │ ───► │    TIER      │   │
│  ├──────────────┤      ├──────────────┤      ├──────────────┤   │
│  │ index.html   │      │ Flask (app.py)│      │ Decision Tree│   │
│  │ result.html  │ ◄─── │ Routes       │ ◄─── │ model.pkl    │   │
│  │ style.css    │      │ Prediction   │      │ Encoders     │   │
│  └──────────────┘      └──────────────┘      └──────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow Diagram

```
User Input → HTTP POST → Flask Backend → Model Prediction → Results Page
     ↓            ↓              ↓                ↓               ↓
   Skills     /predict      LabelEncode    career + probs     Display
```

---

## 📊 Model Performance

### Classification Report

| Career Path | Precision | Recall | F1-Score | Support |
|-------------|:---------:|:------:|:--------:|:-------:|
| 🤖 Artificial Intelligence | 84% | 73% | 78% | 81 |
| 🔒 Cybersecurity | 89% | 90% | 89% | 70 |
| 📊 Data Science | 83% | 91% | 87% | 70 |
| 💻 Software Engineering | 87% | 91% | 89% | 67 |
| 🌐 Web Development | 85% | 85% | 85% | 72 |

### Key Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | **95.0%** |
| Macro Avg F1 | 85.6% |
| Weighted Avg F1 | 85.4% |

### Model Comparison

```
Decision Tree     ████████████████████████████████████████ 95.0%  ✅ BEST
KNN               ████████████████████████████████░░░░░░░░ 81.1%
```

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | Python 3.14 | Core programming language |
| **Web Framework** | Flask | REST API & routing |
| **ML Algorithms** | Scikit-learn | Decision Tree, KNN, Label Encoding |
| **Data Processing** | Pandas, NumPy | Dataset manipulation |
| **Frontend** | HTML5, CSS3, JavaScript | User interface |
| **Animations** | CSS3 Keyframes | Smooth transitions |
| **Typography** | Google Fonts | Sora, JetBrains Mono |

---

## 📁 Project Structure

```
AI-Career-Path-Predictor/
│
├── 📄 app.py                      # Main Flask application
├── 📄 README.md                   # Project documentation
├── 📄 .gitignore                  # Git ignore rules
│
├── 📁 data/
│   └── 📄 career_dataset.csv      # 1,800 samples, 6 features, 5 classes
│
├── 📁 model/
│   ├── 📄 train_model.py          # Model training script
│   └── 📄 model.pkl               # Trained Decision Tree (95% accuracy)
│
├── 📁 templates/
│   ├── 📄 index.html              # Input form page
│   └── 📄 result.html             # Results display page
│
└── 📁 static/
    └── 📄 style.css               # Complete styling (Dark/Light themes)
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Step 1: Clone Repository

```bash
git clone https://github.com/KULSOOM2001/AI-Career-Path-Predictor.git
cd AI-Career-Path-Predictor
```

### Step 2: Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### Step 3: Train the Model

```bash
cd model
python train_model.py
```

**Expected Output:**
```
Dataset loaded: 1800 rows
Train: 1440 | Test: 360
Decision Tree Accuracy: 95.00%
KNN Accuracy: 81.11%
Best Model: Decision Tree (95.00%)
Model saved!
```

### Step 4: Run Application

```bash
cd ..
python app.py
```

### Step 5: Access Application

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 💻 Usage Guide

### Input Fields

| Field | Options |
|-------|---------|
| 📚 Favourite Subject | Mathematics / Programming / Science / Design / Networking / Business |
| 💻 Coding Interest | Low / Medium / High |
| 📐 Math Skill | Low / Medium / High |
| 🎨 Creativity Level | Low / Medium / High |
| 🗣️ Communication Skill | Low / Medium / High |
| 🧩 Problem Solving Skill | Low / Medium / High |

### Output Components

After submission, you'll receive:

1. **Career Match** - Recommended career path with icon
2. **Confidence Score** - Model's certainty percentage with animated progress bar
3. **Key Skills** - Skills to develop for your recommended career
4. **Job Roles** - Possible positions in that field
5. **All Career Scores** - Probability distribution across all 5 careers
6. **Feature Importance** - Visual breakdown of skill impact

---

## 📈 Feature Importance Analysis

The Decision Tree model calculates **Gini Importance** for each feature:

| Rank | Feature | Importance | Impact Level |
|:----:|---------|:----------:|:------------:|
| 1 | 🎨 Creativity Level | **46.8%** | ████████████████████ |
| 2 | 📐 Math Skill | **24.2%** | ██████████ |
| 3 | 🗣️ Communication Skill | **23.6%** | ██████████ |
| 4 | 📚 Favourite Subject | **2.3%** | █ |
| 5 | 💻 Coding Interest | **1.9%** | █ |
| 6 | 🧩 Problem Solving Skill | **1.1%** | ▏ |

> 💡 **Key Insight:** Creativity emerges as the most influential factor for tech career prediction, contributing nearly 47% to the decision-making process.

---

## 🎨 UI/UX Design Showcase

### Design System

| Element | Dark Theme | Light Theme |
|---------|------------|-------------|
| Background | `#060814` | `#f0f4f8` |
| Surface | `#0f1428` | `#ffffff` |
| Accent | `#4ea8ff` | `#4f46e5` |
| Text | `#eef4ee` | `#1e293b` |

### Visual Effects

- ✨ **Scanline Sweep** - Diagonal light animation
- 🔆 **Radar Glow** - Pulsing gradient effect
- 📊 **Animated Progress Bars** - Smooth width transitions
- 🎯 **Hover Effects** - Lift, shadow, and border glow

---

## 🔮 Future Enhancements

| Enhancement | Description | Priority |
|-------------|-------------|:--------:|
| More Career Paths | Add Cloud Computing, DevOps, UI/UX Design | High |
| Real-time Job Data | API integration for live market trends | Medium |
| User Accounts | Save prediction history | Medium |
| PDF Reports | Download career guidance reports | Low |
| Voice Input | Speech-to-text for form filling | Low |

---

<div align="center">

## 🌟 Show Your Support

If this project helped you, please consider giving it a ⭐ on GitHub!

</div>
```
