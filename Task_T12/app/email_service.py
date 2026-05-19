import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import (
    SMTP_EMAIL,
    SMTP_PASSWORD,
    FROM_EMAIL
)

from app.logger_config import logger


def send_welcome_email(data):

    try:

        subject = "Thanks for contacting us"

        body = f"""
Hi {data.name},

Thank you for reaching out to our sales team.

We’ve received your inquiry successfully and a representative will contact you shortly.

Company: {data.company}

Best regards,
Sales Team
"""

        msg = MIMEMultipart()

        msg["From"] = FROM_EMAIL
        msg["To"] = data.email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        server.send_message(msg)

        server.quit()

        logger.info(
            f"Welcome email sent to {data.email}"
        )

    except smtplib.SMTPException as e:

        logger.error(
            f"SMTP error: {str(e)}"
        )

    except Exception as e:

        logger.error(
            f"Email sending failed: {str(e)}"
        )