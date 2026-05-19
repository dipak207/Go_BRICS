from notion_client import Client

from app.config import (
    NOTION_TOKEN,
    NOTION_DATABASE_ID
)

from app.logger_config import logger

from datetime import (
    datetime,
    timedelta
)

import time


notion = Client(auth=NOTION_TOKEN)

def check_duplicate_lead(email: str):

    try:

        response = notion.databases.query(
            database_id=NOTION_DATABASE_ID
        )

        results = response.get("results", [])

        for page in results:

            properties = page.get("properties", {})

            existing_email = (
                properties
                .get("Email", {})
                .get("email")
            )

            if existing_email:

                if existing_email.lower() == email.lower():

                    logger.warning(
                        f"Duplicate lead found: {email}"
                    )

                    return True

        return False

    except Exception as e:

        logger.error(
            f"Duplicate check failed: {str(e)}"
        )

        return False

def create_notion_lead(data):

    for attempt in range(3):

        try:

            # Auto Follow-Up Date
            follow_up_date = (
                datetime.now() + timedelta(days=2)
            ).date().isoformat()

            response = notion.pages.create(

                parent={
                    "database_id": NOTION_DATABASE_ID
                },

                properties={

                    "Lead Name": {
                        "title": [
                            {
                                "text": {
                                    "content": data.name
                                }
                            }
                        ]
                    },

                    "Company": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": data.company
                                }
                            }
                        ]
                    },

                    "Email": {
                        "email": data.email
                    },

                    "Phone": {
                        "phone_number": data.phone
                    },

                    "Status": {
                        "status": {
                            "name": "New Lead"
                        }
                    },

                    "Priority": {
                        "select": {
                            "name": "Medium"
                        }
                    },

                    "Lead Source": {
                        "select": {
                            "name": "Inbound"
                        }
                    },

                    "Follow-Up Date": {
                        "date": {
                            "start": follow_up_date
                        }
                    },

                   
                    "Notes": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": (
                                        "Lead automatically "
                                        "created via FastAPI "
                                        "automation workflow."
                                    )
                                }
                            }
                        ]
                    }

                }
            )

            logger.info(
                f"Lead inserted into Notion CRM: {data.email}"
            )

            return response

        except Exception as e:

            logger.warning(
                f"Notion retry attempt "
                f"{attempt + 1} failed: {str(e)}"
            )

            time.sleep(2)

    logger.error(
        f"Notion insertion permanently failed "
        f"for {data.email}"
    )

    raise Exception(
        "Failed to create lead in Notion"
    )