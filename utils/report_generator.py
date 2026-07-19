"""
utils/report_generator.py
"""

from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

from config import REPORT_DIR

REPORT_DIR.mkdir(
    exist_ok=True
)


def create_report(
    overview,
    metrics,
    insights
):

    path = REPORT_DIR / "DecisionPilot_Report.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(str(path))

    story = []

    story.append(
        Paragraph(
            "<b>DecisionPilot AI Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Dataset Overview</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            str(overview),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Model Metrics</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            str(metrics),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>AI Insights</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            insights.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return path