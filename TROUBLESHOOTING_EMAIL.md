# Email Troubleshooting Guide

## ✅ Current Status: Network Connectivity Confirmed
- Port 465 (SSL) is accessible: ✅ Connection succeeded
- Port 587 (TLS) is blocked: ❌ Connection timed out

## 🔐 Critical Issue: Application-Specific Password Required
The error indicates your Gmail account has 2-factor authentication enabled and requires an app password.

### Steps to Generate App Password:
1. Go to your Google Account settings: https://myaccount.google.com/
2. Navigate to **Security** → **2-Step Verification** (you may need to sign in again)
3. Scroll down to **App passwords**
4. Generate a new app password for "Mail"
5. Copy the 16-character password (it will look like: `abcd efgh ijkl mnop`)
6. Update the `EMAIL_PASSWORD` in `config.py` with this new app password

### Current Configuration in config.py:
```python
EMAIL_USER = "gheecodes381@gmail.com"
EMAIL_PASSWORD = "lllk pnke olnk zgmc"  # ❌ This needs to be replaced with a valid app password
```

### ✅ Working Configuration:
- Use **Port 465 with SSL** (confirmed working for network connectivity)
- Use **App Password** instead of regular password (required for 2FA accounts)

### Test Commands:
```bash
# Test SSL connectivity (port 465)
nc -zv smtp.gmail.com 465

# Test email sending with SSL
python3 -c "from email_alert_alternative import send_email_alert_ssl; send_email_alert_ssl('Test email')"
```

## 🚀 Next Steps:
1. Generate an app password from your Google Account
2. Update the password in `config.py`
3. Test email sending using the SSL version
4. The email alerts should now work successfully!

## Common Gmail SMTP Issues and Solutions

### 1. App Password Setup
If you have 2-factor authentication enabled, you must use an app password:
1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification → App passwords
3. Generate an app password for "Mail"
4. Use this 16-character password in your config.py file

### 2. Allow Less Secure Apps (if 2FA is disabled)
1. Go to your Google Account settings
2. Navigate to Security → Less secure app access
3. Turn on access (not recommended for security)

### 3. Check Gmail Account Settings
- Make sure IMAP is enabled in Gmail settings
- Check if there are any security alerts on your account

### 4. Network/Firewall Issues
- Check if your network allows outbound connections on port 587
- Try using a different network (mobile hotspot)

### 5. Test Connection Manually
You can test SMTP connection using telnet:
```bash
telnet smtp.gmail.com 587
```

### 6. Alternative SMTP Settings
Try using these alternative settings:
- Port: 465 (with SSL instead of TLS)
- Server: smtp.gmail.com

### Quick Test Commands:
```bash
# Test basic connectivity
nc -zv smtp.gmail.com 587

# Test with Python
python3 test_email.py
