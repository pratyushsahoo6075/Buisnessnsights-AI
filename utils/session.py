import streamlit as st

def initialize_session():

    defaults = {

        "raw_data": None,

        "clean_data": None,

        "trained_model": None,

        "target_column": None,

        "task_type": None,

        "model_metrics": {},

        "ai_insights": "",

        "chat_history": []

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value