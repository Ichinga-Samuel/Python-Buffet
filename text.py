import reports
import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

text = """"""
date = datetime.date.today().strftime("%B %d, %Y")
title = "Processed Update on " + date
f = [["Apple", "500 lbs"], ["Avocado", "200 lbs"], ["Grape", "300 lbs"]]
attachment = "./tmp/processed.pdf"
for t in f:
  text += "name: {}".format(t[0]) + "<br/>"
  text += "weight: {}".format(t[1]) + "<br/><br/>"



if __name__ == "__main__":
    reports.generate_report(attachment, title, text)


