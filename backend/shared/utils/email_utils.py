import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config.config import settings
from pathlib import Path


def render_template(template_name: str, variables: dict):
    """Render HTML template with variables"""

    path = Path(template_name)

    # CASE 1: full path passed (tests / temp files)
    if path.exists():
        template_path = path

    # CASE 2: just filename (production templates)
    else:
        template_path = Path("templates/emails") / template_name

        # fallback safety check
        if not template_path.exists():
            raise FileNotFoundError(
                f"Template not found: {template_name}"
            )

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in variables.items():
        content = content.replace(f"{{{{ {key} }}}}", str(value))

    return content


def send_verification_email(to_email: str, otp_code: str):
    """Send OTP email using Gmail SMTP with SSL"""

    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    sender_email = settings.EMAIL_USER
    sender_password = settings.EMAIL_PASS

    print(f"[EMAIL] Sending OTP {otp_code} to {to_email}")

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
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"[EMAIL] OTP {otp_code} sent successfully to {to_email}")
        return True

    except Exception as e:
        print(f"[EMAIL] Failed: {str(e)}")
        return False


def send_welcome_email(to_email: str, first_name: str, organization_name: str):
    """Send welcome email using HTML template with organization name"""

    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    sender_email = settings.EMAIL_USER
    sender_password = settings.EMAIL_PASS

    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = f"Welcome to {organization_name}, {first_name}!"

    # Render HTML template with organization name
    html_content = render_template("welcome.html", {
        "first_name": first_name,
        "email": to_email,
        "organization_name": organization_name
    })

    # Plain text fallback
    text_content = f"""Welcome to {organization_name}, {first_name}!

Your email {to_email} has been verified for {organization_name}.

You now have full access to all features.

Happy coding!
The {organization_name} Team"""

    msg.attach(MIMEText(text_content, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"[WELCOME EMAIL] Sent to {to_email} for {organization_name}")
        return True
    except Exception as e:
        print(f"[WELCOME EMAIL] Failed: {str(e)}")
        return False


def send_inactive_reminder_email(to_email: str, first_name: str, days_inactive: int):
    """Send reminder email to inactive users"""

    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    sender_email = settings.EMAIL_USER
    sender_password = settings.EMAIL_PASS

    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = f"We miss you, {first_name}! 👋"

    html_content = render_template("reminder.html", {
        "first_name": first_name,
        "days_inactive": days_inactive
    })

    text_content = f"""We miss you, {first_name}!

It's been {days_inactive} days since your last visit.

We've added new features and improvements we think you'll love!

Log in now: http://localhost:8000/docs

See you soon!
The FastAPI Team"""

    msg.attach(MIMEText(text_content, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(
            f"[REMINDER EMAIL] Sent to {to_email} ({days_inactive} days inactive)")
        return True
    except Exception as e:
        print(f"[REMINDER EMAIL] Failed: {e}")
        return False
