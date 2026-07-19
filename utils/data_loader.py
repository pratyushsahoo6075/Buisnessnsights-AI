"""
utils/data_loader.py

Handles:
- Upload validation
- CSV/Excel loading
- File saving
- Dataset information
"""

from pathlib import Path

import pandas as pd

from config import (
    SUPPORTED_FILES,
    UPLOAD_DIR
)


# --------------------------------------
# Create upload folder automatically
# --------------------------------------

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------
# Validate uploaded file
# --------------------------------------

def validate_file(uploaded_file):
    """
    Validate uploaded file extension.
    """

    if uploaded_file is None:
        raise ValueError("No file uploaded.")

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension not in SUPPORTED_FILES:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return extension


# --------------------------------------
# Load Dataset
# --------------------------------------

def load_dataset(uploaded_file):
    """
    Load CSV or Excel file.
    """

    extension = validate_file(uploaded_file)

    try:

        if extension == "csv":

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

        return df

    except Exception as e:

        raise RuntimeError(
            f"Unable to read dataset.\n{e}"
        )


# --------------------------------------
# Save Uploaded File
# --------------------------------------

def save_uploaded_file(uploaded_file):
    """
    Save uploaded file to data/uploads
    """

    destination = UPLOAD_DIR / uploaded_file.name

    with open(destination, "wb") as f:

        f.write(uploaded_file.getbuffer())

    return destination


# --------------------------------------
# Dataset Information
# --------------------------------------

def dataset_info(df):
    """
    Return basic dataset information.
    """

    return {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing_values": int(df.isnull().sum().sum()),

        "duplicates": int(df.duplicated().sum()),

        "memory_usage": round(
            df.memory_usage(deep=True).sum() / 1024,
            2
        ),

        "column_names": list(df.columns)
    }