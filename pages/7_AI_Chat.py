import streamlit as st
from utils.session import initialize_session

initialize_session()

from utils.chatbot import ask_dataset_question

st.set_page_config(
    page_title="AI Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Chat With Dataset")

st.markdown("---")

if st.session_state.clean_data is None:
    st.warning("Upload and preprocess a dataset first.")
    st.stop()

df = st.session_state.clean_data

question = st.chat_input(
    "Ask something about your dataset..."
)

if question:

    context = df.head(20).to_string()

    answer = ask_dataset_question(
        question,
        context
    )

    st.session_state.chat_history.append(
        ("You", question)
    )

    st.session_state.chat_history.append(
        ("AI", answer)
    )

for role, message in st.session_state.get("chat_history", []):

    with st.chat_message(role):

        st.write(message)