
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="DecisionPilot AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Session State
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = None

if "clean_data" not in st.session_state:
    st.session_state.clean_data = None

if "model" not in st.session_state:
    st.session_state.model = None

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 DecisionPilot AI")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **AI-Powered Business Analytics**

    Analyze datasets

    Train ML models

    Generate AI Insights

    Export Reports
    """
)

# -----------------------------
# Main Title
# -----------------------------
st.title("📊 DecisionPilot AI")

st.subheader("AI-Powered Business Analytics & Decision Support")

st.markdown("---")

# -----------------------------
# About Project
# -----------------------------
st.header("About")

st.write("""
DecisionPilot AI helps analysts and business users quickly understand datasets,
build machine learning models, and generate AI-powered business insights
through an easy-to-use Streamlit interface.
""")

# -----------------------------
# Features
# -----------------------------
st.header("Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Upload CSV / Excel")
    st.success("✅ Automatic Data Cleaning")
    st.success("✅ Exploratory Data Analysis")

with col2:
    st.success("✅ Machine Learning")
    st.success("✅ AI Business Insights")
    st.success("✅ PDF Report Export")

# -----------------------------
# Workflow
# -----------------------------
st.header("Workflow")

st.code("""
Upload Dataset
      ↓
Clean Data
      ↓
EDA
      ↓
Train ML Model
      ↓
AI Insights
      ↓
Generate Report
""")

# -----------------------------
# Tech Stack
# -----------------------------
st.header("Tech Stack")

st.write("""
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- XGBoost
- Google Gemini/OpenAI
- ReportLab
""")

st.markdown("---")

st.caption("Built using Python, Machine Learning, and Generative AI.")