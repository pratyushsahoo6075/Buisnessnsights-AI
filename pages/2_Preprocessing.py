import streamlit as st

from utils.preprocessing import (
    get_summary,
    missing_report,
    clean_dataset
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Data Preprocessing",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Preprocessing")

st.write(
    "Analyze dataset quality and clean missing values and duplicate records."
)

st.markdown("---")

# =====================================================
# CHECK DATASET
# =====================================================

if st.session_state.raw_data is None:

    st.warning("Please upload a dataset first.")

    st.stop()

df = st.session_state.raw_data

# =====================================================
# DATASET SUMMARY
# =====================================================

summary = get_summary(df)

st.subheader("Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", summary["rows"])

col2.metric("Columns", summary["columns"])

col3.metric("Missing Values", summary["missing"])

col4.metric("Duplicate Rows", summary["duplicates"])

st.markdown("---")

# =====================================================
# MISSING VALUE REPORT
# =====================================================

st.subheader("Missing Value Report")

report = missing_report(df)

st.dataframe(
    report,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# PREVIEW
# =====================================================

st.subheader("Raw Dataset")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CLEAN BUTTON
# =====================================================

if st.button(
    "🧹 Clean Dataset",
    use_container_width=True
):

    with st.spinner("Cleaning dataset..."):

        clean_df, removed = clean_dataset(df)

        st.session_state.clean_data = clean_df

    st.success("Dataset cleaned successfully.")

    st.markdown("---")

    st.subheader("Cleaning Summary")

    before = get_summary(df)

    after = get_summary(clean_df)

    c1, c2 = st.columns(2)

    with c1:

        st.write("### Before")

        st.metric("Rows", before["rows"])

        st.metric("Missing", before["missing"])

        st.metric("Duplicates", before["duplicates"])

    with c2:

        st.write("### After")

        st.metric("Rows", after["rows"])

        st.metric("Missing", after["missing"])

        st.metric("Duplicates", after["duplicates"])

    st.info(f"Duplicate rows removed: {removed}")

    st.markdown("---")

    st.subheader("Cleaned Dataset")

    st.dataframe(
        clean_df.head(10),
        use_container_width=True
    )

    st.success(
        "Dataset is ready for Exploratory Data Analysis."
    )