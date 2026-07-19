import streamlit as st
import pandas as pd
from utils.session import initialize_session

initialize_session()

from utils.model import train_model

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning")

st.markdown("---")

# ==========================================================
# CHECK DATA
# ==========================================================

if st.session_state.clean_data is None:

    st.warning("Please preprocess your dataset first.")

    st.stop()

df = st.session_state.clean_data

# ==========================================================
# TARGET COLUMN
# ==========================================================

target = st.selectbox(
    "Select Target Column",
    df.columns
)

# ==========================================================
# AUTO DETECT TASK
# ==========================================================

target_dtype = df[target].dtype

if str(target_dtype) in ["object", "category"]:

    task = "Classification"

elif df[target].nunique() <= 10:

    task = "Classification"

else:

    task = "Regression"

st.info(f"Detected Task : **{task}**")

# ==========================================================
# MODEL LIST
# ==========================================================

if task == "Classification":

    algorithms = [

        "Logistic Regression",

        "Decision Tree",

        "Random Forest"

    ]

else:

    algorithms = [

        "Linear Regression",

        "Decision Tree",

        "Random Forest"

    ]

algorithm = st.selectbox(

    "Select Algorithm",

    algorithms

)

st.markdown("---")

# ==========================================================
# TRAIN
# ==========================================================

if st.button(
    "🚀 Train Model",
    use_container_width=True
):

    with st.spinner("Training Model..."):

        model, metrics = train_model(

            df=df,

            target=target,

            algorithm=algorithm,

            task_type=task

        )

    st.session_state.trained_model = model

    st.session_state.target_column = target

    st.session_state.task_type = task

    st.session_state.model_metrics = metrics

    st.success("Model Trained Successfully")

    st.markdown("---")

    st.subheader("Evaluation Metrics")

    cols = st.columns(len(metrics))

    for column, (metric, value) in zip(cols, metrics.items()):

        column.metric(

            metric,

            f"{value:.4f}"

        )

st.markdown("---")

# ==========================================================
# MODEL INFORMATION
# ==========================================================

if st.session_state.trained_model is not None:

    st.subheader("Current Model")

    c1, c2 = st.columns(2)

    c1.write(
        "**Algorithm**"
    )

    c1.success(
        algorithm
    )

    c2.write(
        "**Task Type**"
    )

    c2.success(
        task
    )

    st.success(
        "Model saved to models/trained_model.pkl"
    )