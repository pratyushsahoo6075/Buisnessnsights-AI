"""
utils/insights.py
"""

from utils.prompts import business_insights_prompt
from services.gemini_service import generate_text


def generate_business_insights(
    dataset_info,
    statistics
):
    """
    Generate AI business insights.
    """

    prompt = business_insights_prompt(
        dataset_info,
        statistics
    )

    return generate_text(prompt)