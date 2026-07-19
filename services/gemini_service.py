"""
services/gemini_service.py

Handles all communication with Google Gemini.
"""

import os

import google.generativeai as genai

from dotenv import load_dotenv

from config import LLM_MODEL


# ==========================================
# Load Environment
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# ==========================================
# Configure Gemini
# ==========================================

if API_KEY:

    genai.configure(api_key=API_KEY)

    MODEL = genai.GenerativeModel(
        model_name=LLM_MODEL
    )

else:

    MODEL = None


# ==========================================
# Check API
# ==========================================

def api_available():

    return MODEL is not None


# ==========================================
# Generate Response
# ==========================================

def generate_text(prompt):

    if MODEL is None:

        raise RuntimeError(
            "Gemini API Key not found.\n"
            "Please configure GEMINI_API_KEY in your .env file."
        )

    try:

        response = MODEL.generate_content(prompt)

        return response.text

    except Exception as e:

        raise RuntimeError(
            f"Gemini Error:\n{str(e)}"
        )