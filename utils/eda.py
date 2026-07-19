"""
utils/eda.py

EDA utility functions.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# DATASET OVERVIEW
# ==========================================================

def dataset_overview(df: pd.DataFrame):

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Numeric Columns": len(df.select_dtypes(include="number").columns),
        "Categorical Columns": len(df.select_dtypes(exclude="number").columns),
        "Memory (KB)": round(
            df.memory_usage(deep=True).sum() / 1024,
            2
        )
    }


# ==========================================================
# DATA TYPES
# ==========================================================

def datatype_summary(df):

    return pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })


# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

def descriptive_statistics(df):

    return df.describe(include="all").transpose()


# ==========================================================
# MISSING VALUES
# ==========================================================

def missing_summary(df):

    missing = df.isnull().sum()

    report = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    return report


# ==========================================================
# CORRELATION
# ==========================================================

def correlation_chart(df):

    numeric = df.select_dtypes(include="number")

    if numeric.shape[1] < 2:
        return None

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        title="Correlation Heatmap"
    )

    return fig


# ==========================================================
# HISTOGRAM
# ==========================================================

def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Distribution of {column}"
    )

    return fig


# ==========================================================
# BOXPLOT
# ==========================================================

def boxplot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"Boxplot of {column}"
    )

    return fig


# ==========================================================
# SCATTER PLOT
# ==========================================================

def scatter_plot(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        title=f"{x} vs {y}"
    )

    return fig


# ==========================================================
# BAR CHART
# ==========================================================

def category_chart(df, column):

    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = ["Category", "Count"]

    fig = px.bar(
        counts,
        x="Category",
        y="Count",
        title=f"{column} Distribution"
    )

    return fig