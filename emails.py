import smtplib
import poplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_gmail(sender, recipient, subject, message, secure=True):
    SMTP_SERVER = 'smtp.google.com'
    SMTP_PORT = 587
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    if secure:
        session.starttls()
        password = getpass.getpass(prompt='Enter Your Password')
        session.login(sender, password)

    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    msg['Subject'] = subject
    part = MIMEText('text', 'plain')
    message_text = message
    part.set_payload(message_text)
    msg.attach(part)
    session.sendmail('sender', 'recipient', msg.as_string())
    session.quit()


def fetch_gmail(username, password):
    server = 'pop.googlemail.com'
    port = 995

    mb = poplib.POP3_SSl(server, port)
    mb.user(username)
    mb.pass_(password)
    num_msg = len(mb.list()[1])
    for n in mb.retr(1)[1]:
        print(n)
    mb.quit()
