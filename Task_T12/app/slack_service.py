import requests

from app.config import SLACK_WEBHOOK_URL
from app.logger_config import logger


def send_slack_notification(data):

    try:

        message = {
            "text": (
                f"🚀 New Lead Received\n\n"
                f"👤 Name: {data.name}\n"
                f"🏢 Company: {data.company}\n"
                f"📧 Email: {data.email}\n"
                f"📱 Phone: {data.phone}\n"
                f"📌 Status: New Lead"
            )
        }

        response = requests.post(
            SLACK_WEBHOOK_URL,
            json=message,
            timeout=10
        )

        response.raise_for_status()

        logger.info(
            f"Slack notification sent for {data.email}"
        )

    except requests.exceptions.Timeout:

        logger.error(
            "Slack webhook timeout"
        )

    except Exception as e:

        logger.error(
            f"Slack notification failed: {str(e)}"
        )