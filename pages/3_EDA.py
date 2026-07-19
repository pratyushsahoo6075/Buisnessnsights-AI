import streamlit as st

from utils.eda import (
    dataset_overview,
    datatype_summary,
    descriptive_statistics,
    missing_summary,
    correlation_chart,
    histogram,
    boxplot,
    scatter_plot,
    category_chart
)

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis")

st.markdown("---")

# ==========================================================
# CHECK DATA
# ==========================================================

if st.session_state.clean_data is None:

    st.warning("Please preprocess your dataset first.")

    st.stop()

df = st.session_state.clean_data

overview = dataset_overview(df)

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Rows", overview["Rows"])
c2.metric("Columns", overview["Columns"])
c3.metric("Numeric", overview["Numeric Columns"])
c4.metric("Categorical", overview["Categorical Columns"])
c5.metric("Memory (KB)", overview["Memory (KB)"])

st.markdown("---")

# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📄 Overview",
        "📈 Distribution",
        "📉 Relationships",
        "📋 Statistics"
    ]
)

# ==========================================================
# OVERVIEW
# ==========================================================

with tab1:

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.subheader("Data Types")

    st.dataframe(
        datatype_summary(df),
        use_container_width=True
    )

    st.subheader("Missing Values")

    st.dataframe(
        missing_summary(df),
        use_container_width=True
    )

# ==========================================================
# DISTRIBUTION
# ==========================================================

with tab2:

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        selected = st.selectbox(
            "Numeric Column",
            numeric_columns
        )

        st.plotly_chart(
            histogram(df, selected),
            use_container_width=True
        )

        st.plotly_chart(
            boxplot(df, selected),
            use_container_width=True
        )

    categorical_columns = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    if categorical_columns:

        cat = st.selectbox(
            "Categorical Column",
            categorical_columns
        )

        st.plotly_chart(
            category_chart(df, cat),
            use_container_width=True
        )

# ==========================================================
# RELATIONSHIPS
# ==========================================================

with tab3:

    heatmap = correlation_chart(df)

    if heatmap is not None:

        st.plotly_chart(
            heatmap,
            use_container_width=True
        )

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) >= 2:

        x = st.selectbox(
            "X Axis",
            numeric_columns,
            key="scatter_x"
        )

        y = st.selectbox(
            "Y Axis",
            numeric_columns,
            index=1,
            key="scatter_y"
        )

        st.plotly_chart(
            scatter_plot(df, x, y),
            use_container_width=True
        )

# ==========================================================
# STATISTICS
# ==========================================================

with tab4:

    st.dataframe(
        descriptive_statistics(df),
        use_container_width=True
    )

    csv = descriptive_statistics(df).to_csv().encode("utf-8")

    st.download_button(
        "📥 Download Statistics",
        data=csv,
        file_name="eda_statistics.csv",
        mime="text/csv"
    )