"""
utils/prompts.py

Prompt templates used across DecisionPilot AI.
"""

# ==========================================================
# DATASET SUMMARY
# ==========================================================

def dataset_summary_prompt(dataset_info, columns):
    return f"""
You are an expert Data Analyst.

Analyze the following dataset.

Dataset Information

{dataset_info}

Columns

{columns}

Provide:

1. Dataset overview
2. Possible business domain
3. Important columns
4. Potential challenges
5. Initial observations

Keep the response professional and concise.
"""


# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

def business_insights_prompt(dataset_info, statistics):
    return f"""
You are a Senior Business Analyst.

Dataset Information

{dataset_info}

Statistics

{statistics}

Generate:

• Executive Summary

• Key Insights

• Business Opportunities

• Risks

• Recommendations

Write in business language suitable for management.
"""


# ==========================================================
# EXECUTIVE REPORT
# ==========================================================

def executive_report_prompt(
    dataset_info,
    model_metrics,
    statistics
):
    return f"""
Create an executive business report.

Dataset

{dataset_info}

Model Performance

{model_metrics}

Statistics

{statistics}

Include:

1. Executive Summary

2. Dataset Overview

3. Key Findings

4. Model Performance

5. Business Impact

6. Strategic Recommendations

Professional tone.
"""
# ==========================================================
# CHATBOT
# ==========================================================

def chatbot_prompt(question, dataset_context):
    return f"""
You are an AI Data Analyst.

Dataset Context

{dataset_context}

User Question

{question}

Answer accurately.

If the answer cannot be determined from the dataset,
state that clearly instead of making assumptions.
"""