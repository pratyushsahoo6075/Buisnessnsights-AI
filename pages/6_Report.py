import streamlit as st

from utils.eda import dataset_overview
from utils.report_generator import create_report

st.set_page_config(
    page_title="Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Generate Report")

st.markdown("---")

if st.session_state.clean_data is None:

    st.warning("Please complete previous steps.")

    st.stop()

overview = dataset_overview(
    st.session_state.clean_data
)

metrics = st.session_state.model_metrics

insights = st.session_state.ai_insights

if st.button(
    "📄 Generate PDF Report",
    use_container_width=True
):

    pdf_path = create_report(
        overview,
        metrics,
        insights or "No AI insights generated."
    )

    st.success("Report Generated")

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            "⬇ Download PDF",
            pdf,
            file_name="DecisionPilot_Report.pdf",
            mime="application/pdf"
        )