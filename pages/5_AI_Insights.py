import streamlit as st

from utils.insights import generate_business_insights
from utils.eda import (
    dataset_overview,
    descriptive_statistics
)

st.set_page_config(
    page_title="AI Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AI Business Insights")

st.markdown("---")

if st.session_state.clean_data is None:
    st.warning("Please preprocess your dataset first.")
    st.stop()

df = st.session_state.clean_data

overview = dataset_overview(df)
statistics = descriptive_statistics(df)

if st.button(
    "✨ Generate AI Insights",
    use_container_width=True
):

    with st.spinner("Generating insights..."):

        insights = generate_business_insights(
            overview,
            statistics
        )

    st.session_state.ai_insights = insights

if st.session_state.ai_insights:

    st.subheader("Executive Summary")

    st.markdown(
        st.session_state.ai_insights
    )

    st.download_button(
        "Download Insights",
        st.session_state.ai_insights,
        file_name="AI_Insights.txt"
    )