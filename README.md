# 📰 Fake News Detector

> AI-powered Fake News Detection using **Natural Language Processing (NLP)** and **Machine Learning**.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🚀 Live Demo

🔗 https://fake-news-ai-detecter.streamlit.app/

---

## 📌 Overview

Fake News Detector is an NLP-based Machine Learning application that predicts whether a news article is **Real** or **Fake**.

The project uses **TF-IDF Vectorization** for text feature extraction and a **Linear Support Vector Machine (Linear SVM)** classifier to achieve high prediction accuracy.

---

## ✨ Features

- 📰 Detect Fake & Real News
- 🤖 Machine Learning Based Prediction
- 📊 TF-IDF Text Vectorization
- ⚡ Fast Real-Time Prediction
- 💻 Interactive Streamlit Web App
- 🎯 99.30% Accuracy
- 🌐 Live Deployment

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLP
- TF-IDF
- Linear SVM

---

## 📂 Project Structure

```text
Fake-News-Detector
│
├── app.py
├── style.css
├── requirements.txt
├── README.md
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
│
├── notebook
│   └── fake news.ipynb
│
└── dataset
    ├── Fake.csv
    └── True.csv
```

---

## ⚙️ Machine Learning Workflow

```
News Article
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Linear SVM Model
      │
      ▼
Prediction
      │
      ├── ✅ Real News
      └── ❌ Fake News
```

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 98.76% |
| Multinomial Naive Bayes | 93.43% |
| **Linear SVM** ⭐ | **99.30%** |
| Passive Aggressive | 99.27% |

---

## 📊 Dataset

**ISOT Fake and Real News Dataset**

- Fake Articles : **23,481**
- Real Articles : **21,417**
- Total Articles : **44,898**

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/priyanshuso/fake-news-detector-.git
```

Go to project directory

```bash
cd fake-news-detector-
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Confidence Score
- Explainable AI
- News URL Detection
- Multi-language Support
- Generative AI Integration
- News Summarization

---

## 👨‍💻 Developer

**Priyanshu Soni**

B.Tech Computer Science & Engineering (Data Science)

- 🌐 Portfolio: https://priyanshu-soni-portfolio.vercel.app/
- 💼 LinkedIn: https://www.linkedin.com/in/priyanshusoni95/
- 💻 GitHub: https://github.com/priyanshuso

---

## ⭐ Support

If you like this project, don't forget to ⭐ star the repository.

---
