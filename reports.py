# reports.py
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    t = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    header = Paragraph(title, styles["h1"])
    main = Paragraph(paragraph)
    t.build([header, main])