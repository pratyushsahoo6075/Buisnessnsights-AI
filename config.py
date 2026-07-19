from pathlib import Path

# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
SAMPLE_DATA_DIR = DATA_DIR / "sample"

MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"

ASSETS_DIR = BASE_DIR / "assets"

# =====================================================
# APPLICATION
# =====================================================

APP_NAME = "DecisionPilot AI"

APP_VERSION = "2.0"

APP_DESCRIPTION = (
    "AI-Powered Business Analytics & Decision Support Platform"
)

PAGE_ICON = "📊"

LAYOUT = "wide"

# =====================================================
# FILE SETTINGS
# =====================================================

SUPPORTED_FILES = [
    "csv",
    "xlsx",
    "xls"
]

MAX_UPLOAD_SIZE_MB = 200

# =====================================================
# DATA PREPROCESSING
# =====================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

NUMERIC_FILL = "median"

CATEGORICAL_FILL = "mode"

# =====================================================
# MACHINE LEARNING
# =====================================================

CLASSIFICATION_MODELS = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "XGBoost"
]

REGRESSION_MODELS = [
    "Linear Regression",
    "Decision Tree",
    "Random Forest",
    "XGBoost"
]

# =====================================================
# REPORT
# =====================================================

REPORT_NAME = "DecisionPilot_Report.pdf"

# =====================================================
# GEMINI
# =====================================================

LLM_MODEL = "gemini-2.5-flash"

# =====================================================
# STREAMLIT THEME
# =====================================================

PRIMARY_COLOR = "#2563EB"

BACKGROUND_COLOR = "#FFFFFF"

SIDEBAR_COLOR = "#F8FAFC"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

ERROR_COLOR = "#DC2626"