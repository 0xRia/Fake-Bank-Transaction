#!/usr/bin/env python3

from logger import log_transaction
from fraud_engine import is_fraudulent
from email_alert import send_email_alert
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Amount must be positive"
        return True, amount
    except ValueError:
        return False, "Invalid amount format"

def validate_account(account):
    if not account.isdigit() or len(account) != 8:
        return False
    return True

def main():
    # Get transaction details
    amount_str = input("Enter Amount: £")
    is_valid, amount_or_error = validate_amount(amount_str)
    if not is_valid:
        print(f"Error: {amount_or_error}")
        return

    receiver = input("Enter Receiver Account: ")
    if not validate_account(receiver):
        print("Error: Invalid account number format. Must be 8 digits.")
        return

    reason = input("Enter Reason for Transfer: ")
    if not reason.strip():
        print("Error: Reason cannot be empty")
        return

    # Create transaction dictionary
    transaction = {
        'amount': amount_or_error,
        'account_to': receiver,
        'reason': reason
    }

    # Log the transaction
    log_transaction(amount_or_error, receiver, reason)

    # Process the transaction
    process_transaction(transaction)

def process_transaction(transaction):
    flagged, reason = is_fraudulent(transaction)
    if flagged:
        alert_message = f"Fraud alert! Transaction flagged: {reason}\nDetails: {transaction}"
        print(alert_message)  # for debugging
        send_email_alert(alert_message)  # send alert email
    else:
        print("Transaction looks safe.")

if __name__ == "__main__":
    main()
