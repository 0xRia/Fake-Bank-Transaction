#!/usr/bin/env python3


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(message, subject="Fraud Alert", to_email="gheecodes381@gmail.com"):
    from config import EMAIL_USER, EMAIL_PASSWORD
    from_email = EMAIL_USER
    password = EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        print("Sending email...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("✅ Email alert sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")