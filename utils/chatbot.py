"""
utils/chatbot.py
"""

from utils.prompts import chatbot_prompt
from services.gemini_service import generate_text


def ask_dataset_question(
    question,
    dataset_context
):

    prompt = chatbot_prompt(
        question,
        dataset_context
    )

    return generate_text(prompt)