from fastapi import FastAPI, HTTPException

from app.validator import LeadModel
from app.logger_config import logger

from app.notion_service import (
    create_notion_lead,
    check_duplicate_lead
)

from app.slack_service import send_slack_notification
from app.email_service import send_welcome_email

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Lead Automation API Running"
    }


@app.post("/new-lead")
async def create_lead(lead: LeadModel):

    logger.info(f"Lead received: {lead.email}")

    try:

        # Duplicate Check
        if check_duplicate_lead(lead.email):

            logger.warning(
                f"Duplicate lead detected: {lead.email}"
            )

            raise HTTPException(
                status_code=409,
                detail="Duplicate lead already exists"
            )

        # Create CRM Lead
        create_notion_lead(lead)

        # Slack Notification
        send_slack_notification(lead)

        # Welcome Email
        send_welcome_email(lead)

        logger.info(
            f"Lead workflow completed: {lead.email}"
        )

        return {
            "status": "success",
            "message": "Lead added successfully to CRM"
        }

    except HTTPException:
        raise

    except Exception as e:

        logger.error(
            f"Workflow failed: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail={
                "status": "failed",
                "stage": "workflow",
                "message": str(e)
            }
        )