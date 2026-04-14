import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config.config import settings


def send_verification_email(to_email: str, otp_code: str):
    """Send OTP email using Gmail SMTP with SSL"""

    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    sender_email = settings.EMAIL_USER
    sender_password = settings.EMAIL_PASS    # No spaces!

    print(f"[EMAIL] Sending OTP {otp_code} to {to_email}")

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = "Your Verification OTP"

    body = f"""Hello,

Your verification OTP is: {otp_code}

This OTP expires in 24 hours.

If you didn't request this, please ignore this email.

Best regards,
Your App Team
"""
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SSL connection
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"[EMAIL] OTP {otp_code} sent successfully to {to_email}")
        return True

    except Exception as e:
        print(f"[EMAIL] Failed: {str(e)}")
        return False
