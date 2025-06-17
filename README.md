# 🏨 Hybrid Hotel Recommendation System with Sentiment Analysis

This project combines a **deep learning-based sentiment classifier** with a **Flask web application** to recommend hotels based on **user-selected amenities** and **review sentiment scores**. It uses both **machine learning (CNN)** and **lexicon-based (TextBlob + NLTK)** approaches to generate more reliable sentiment predictions for better hotel recommendations.

---

## 🚀 Features

### 💡 Sentiment Analysis
- CNN-based multi-class classifier (positive, neutral, negative)
- Hyperparameter tuning with Keras Tuner
- Lexicon-based scoring using `TextBlob` and `NLTK Opinion Lexicon`
- Hybrid sentiment prediction (weighted average: 70% ML + 30% Lexicon)

### 🧭 Hotel Recommendation (Flask App)
- Users select desired amenities via web interface
- Hotels are filtered based on selected amenities
- Sentiment scores are computed from review text
- Hotels ranked by review sentiment and displayed dynamically

---

## 🧠 Sentiment Analysis Model Architecture

- **Embedding Layer**
- **Conv1D → Global Max Pooling**
- **Dense Layers with Dropout**
- **Softmax Activation** for multi-class classification

Trained on: [Tripadvisor Hotel Reviews Dataset]

---

## 🧪 Hybrid Sentiment Calculation

```python
sentiment_score = 0.7 * ml_score + 0.3 * lexicon_score
