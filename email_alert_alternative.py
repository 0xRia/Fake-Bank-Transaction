#!/usr/bin/env python3

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_USER, EMAIL_PASSWORD

def send_email_alert_ssl(message, subject="Fraud Alert", to_email="gheecodes381@gmail.com"):
    """
    Alternative email sending function using SSL on port 465
    """
    from_email = EMAIL_USER
    password = EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        print("Sending email using SSL...")
        # Create SSL context
        context = ssl.create_default_context()
        
        # Connect using SSL on port 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        
        print("✅ Email alert sent using SSL!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# Test function
def test_ssl_connection():
    print("Testing SSL connection to Gmail...")
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context, timeout=10) as server:
            print("✅ SSL Connection successful")
            return True
    except Exception as e:
        print(f"❌ SSL Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_ssl_connection()
