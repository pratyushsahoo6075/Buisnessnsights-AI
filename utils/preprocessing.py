"""
utils/preprocessing.py

Data preprocessing utilities.
"""

import pandas as pd


# ==========================================================
# Dataset Summary
# ==========================================================

def get_summary(df: pd.DataFrame) -> dict:
    """
    Return dataset quality summary.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum())
    }


# ==========================================================
# Missing Value Report
# ==========================================================

def missing_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return missing value report.
    """

    report = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values,
        "Percentage": (
            df.isnull().mean() * 100
        ).round(2).values
    })

    return report.sort_values(
        by="Missing Values",
        ascending=False
    )


# ==========================================================
# Duplicate Removal
# ==========================================================

def remove_duplicates(df: pd.DataFrame):

    before = len(df)

    clean_df = df.drop_duplicates().copy()

    removed = before - len(clean_df)

    return clean_df, removed


# ==========================================================
# Missing Value Handling
# ==========================================================

def fill_missing_values(df: pd.DataFrame):

    clean_df = df.copy()

    numeric_cols = clean_df.select_dtypes(
        include=["number"]
    ).columns

    categorical_cols = clean_df.select_dtypes(
        include=["object", "category"]
    ).columns

    # Numeric → Median
    for col in numeric_cols:

        clean_df[col] = clean_df[col].fillna(
            clean_df[col].median()
        )

    # Categorical → Mode
    for col in categorical_cols:

        mode = clean_df[col].mode()

        if not mode.empty:

            clean_df[col] = clean_df[col].fillna(mode[0])

        else:

            clean_df[col] = clean_df[col].fillna("Unknown")

    return clean_df


# ==========================================================
# Complete Cleaning Pipeline
# ==========================================================

def clean_dataset(df: pd.DataFrame):

    clean_df = df.copy()

    clean_df, removed_duplicates = remove_duplicates(
        clean_df
    )

    clean_df = fill_missing_values(clean_df)

    return clean_df, removed_duplicates