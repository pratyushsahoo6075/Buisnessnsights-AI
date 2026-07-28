
# 🚀 Business Insight-AI
### AI-Powered Business Intelligence & Decision Support Platform

DecisionPilot AI is an end-to-end **Business Intelligence (BI), Machine Learning, and Generative AI** platform built with **Streamlit**. It enables users to upload datasets, perform automated data preprocessing, explore interactive dashboards, train machine learning models, generate AI-powered business insights, chat with their data, and export professional reports—all within a single application.

Unlike traditional analytics dashboards, DecisionPilot AI combines **Business Intelligence**, **Machine Learning**, and **Large Language Models (LLMs)** to assist in data-driven decision-making.

---

# ✨ Features

## 📂 Data Upload

- Upload CSV and Excel datasets
- Automatic dataset validation
- Dataset preview
- File information
- Data profiling

---

## 🧹 Data Preprocessing

Automatically cleans the dataset by:

- Handling missing values
- Removing duplicate records
- Fixing inconsistent data types
- Data quality summary
- Before vs After comparison

---

## 📊 Exploratory Data Analysis (EDA)

Interactive analytics dashboard including:

- Dataset overview
- Statistical summary
- Data type analysis
- Missing value analysis
- Correlation heatmap
- Histograms
- Box plots
- Scatter plots
- Category distributions

---

## 📈 Business Intelligence Dashboard

Power BI–inspired dashboard that automatically generates:

- KPI Cards
- Business metrics
- Trend analysis
- Distribution charts
- Correlation analysis
- Feature relationships
- Interactive visualizations

---

## 🤖 Machine Learning

Supports both:

### Classification

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost *(optional future enhancement)*

### Regression

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor *(optional future enhancement)*

Features include:

- Automatic task detection
- Recommended model selection
- Manual model selection
- Model evaluation
- Model persistence
- Prediction pipeline

---

## 💡 AI Business Insights

Powered by **Google Gemini**.

Generates:

- Executive Summary
- Business Opportunities
- Business Risks
- Key Findings
- Recommendations
- Decision Support

AI responses are generated using:

- Dataset profile
- EDA statistics
- Machine learning metrics
- Business KPIs

---

## 💬 AI Data Chat

Chat with your dataset using natural language.

Examples:

- Which feature impacts the target most?
- Explain the model performance.
- What business risks are present?
- Summarize this dataset.
- Give recommendations to improve sales.

---

## 📄 Automated Report Generation

Generate downloadable reports containing:

- Dataset overview
- Data preprocessing summary
- EDA findings
- Machine learning metrics
- AI-generated business insights
- Strategic recommendations

---

# 🏗️ Project Workflow


Upload Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Business Intelligence Dashboard
      │
      ▼
Machine Learning
      │
      ▼
AI Business Insights
      │
      ▼
AI Chat Assistant
      │
      ▼
PDF Report


# 📂 Project Structure


DecisionPilot-AI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
│
├── assets/
├── data/
│   ├── uploads/
│   └── sample/
│
├── models/
├── reports/
│
├── pages/
│   ├── 1_Upload.py
│   ├── 2_Preprocessing.py
│   ├── 3_EDA.py
│   ├── 4_ML_Model.py
│   ├── 5_AI_Insights.py
│   ├── 6_Report.py
│   └── 7_AI_Chat.py
│
├── services/
│   └── gemini_service.py
│
└── utils/
    ├── chatbot.py
    ├── data_loader.py
    ├── eda.py
    ├── insights.py
    ├── model.py
    ├── preprocessing.py
    ├── prompts.py
    ├── report_generator.py
    └── session.py
```

---

# ⚙️ Technology Stack

## Frontend

- Streamlit
- Plotly

## Backend

- Python

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Joblib

## AI

- Google Gemini API

## Reporting

- ReportLab

## Environment Management

- Python Dotenv

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/DecisionPilot-AI.git
```

Move into the project

```bash
cd DecisionPilot-AI
```

Create a virtual environment

```bash
py -3.10 -m venv .venv
```

Activate it

Windows

```bash
.\.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 🖥️ Application Flow

```
Home
 │
 ├── Upload Dataset
 │
 ├── Data Cleaning
 │
 ├── Exploratory Data Analysis
 │
 ├── Business Intelligence Dashboard
 │
 ├── Machine Learning
 │
 ├── AI Business Insights
 │
 ├── AI Chat
 │
 └── Generate Report
```

---

# 📈 Future Enhancements

- AutoML model comparison
- SHAP Explainable AI
- Time-series forecasting
- SQL database connectivity
- Multi-user authentication
- Cloud deployment (Azure/AWS/GCP)
- Docker support
- Role-based dashboards
- Interactive KPI drill-downs
- Real-time data streaming
- LLM provider selection (Gemini/OpenAI/Ollama)

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Data Cleaning
- Exploratory Data Analysis
- Business Intelligence
- Data Visualization
- Machine Learning
- Classification & Regression
- Model Evaluation
- Streamlit Application Development
- Prompt Engineering
- Large Language Models
- Google Gemini Integration
- AI-powered Decision Support
- Report Automation

---

# 👨‍💻 Author

**Pratyush Sahoo**

**Tech Stack:** Python • Streamlit • Scikit-learn • Plotly • Google Gemini • Pandas • Machine Learning • Business Intelligence

---

# 📜 License

This project is released under the **MIT License** and is intended for educational, research, and portfolio purposes.

---

# ⭐ Why DecisionPilot AI?

DecisionPilot AI is more than a traditional machine learning application. It combines **Business Intelligence**, **Interactive Analytics**, **Machine Learning**, and **Generative AI** into a unified decision-support platform. By integrating automated preprocessing, visual analytics, predictive modeling, AI-generated business recommendations, and conversational data analysis, it demonstrates a complete end-to-end data science workflow suitable for real-world business scenarios and professional portfolios.
````

