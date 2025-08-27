#!/usr/bin/env python3

import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_USER, EMAIL_PASSWORD

def test_email_connection():
    print("Testing email connection...")
    
    try:
        # Test SMTP connection with timeout
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        print("✅ Connected to SMTP server")
        
        server.starttls()
        print("✅ TLS started")
        
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        print("✅ Login successful")
        
        server.quit()
        print("✅ Connection closed successfully")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        return False
    except socket.timeout:
        print("❌ Connection timeout - check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_email_connection()
