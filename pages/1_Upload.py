import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_dataset,
    save_uploaded_file,
    dataset_info
)

from config import SUPPORTED_FILES

st.set_page_config(page_title="Upload Dataset", page_icon="📂")

st.title("📂 Upload Dataset")

st.write(
    "Upload a CSV or Excel dataset to begin your analysis."
)

st.markdown("---")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=SUPPORTED_FILES
)

if uploaded_file is not None:

    try:

        # -----------------------------
        # Save Uploaded File
        # -----------------------------

        file_path = save_uploaded_file(uploaded_file)

        # -----------------------------
        # Load Dataset
        # -----------------------------

        df = load_dataset(uploaded_file)

        # Store in session
        st.session_state.raw_data = df

        info = dataset_info(df)

        st.success("Dataset uploaded successfully.")

        # -----------------------------
        # Dataset Metrics
        # -----------------------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", info["rows"])

        col2.metric("Columns", info["columns"])

        col3.metric("Missing Values", info["missing_values"])

        col4.metric("Duplicate Rows", info["duplicates"])

        st.markdown("---")

        # -----------------------------
        # Dataset Preview
        # -----------------------------

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        # -----------------------------
        # Dataset Information
        # -----------------------------

        st.subheader("Dataset Information")

        info_col1, info_col2 = st.columns(2)

        with info_col1:

            st.write("**File Name**")
            st.write(uploaded_file.name)

            st.write("**Saved To**")
            st.code(str(file_path))

            st.write("**Memory Usage (KB)**")
            st.write(info["memory_usage"])

        with info_col2:

            st.write("**Column Names**")

            st.dataframe(
                pd.DataFrame(
                    info["column_names"],
                    columns=["Columns"]
                ),
                use_container_width=True
            )

        st.markdown("---")

        st.success(
            "Dataset is ready. Go to the Preprocessing page."
        )

    except Exception as e:

        st.error(str(e))

else:

    st.info(
        "Upload a dataset to continue."
    )