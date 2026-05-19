# Lead Automation Workflow

A multi-step automation workflow built using FastAPI, Notion CRM, Slack Webhooks, and Gmail SMTP.

## Features

- Lead intake API
- Payload validation
- Duplicate lead detection
- Notion CRM integration
- Slack notifications
- Automated welcome emails
- Structured logging
- Retry logic and error handling

## Tech Stack

- FastAPI
- Python
- Notion API
- Slack Incoming Webhooks
- Gmail SMTP

## Workflow

Lead Submission
→ Validation
→ Duplicate Check
→ Notion CRM Insert
→ Slack Alert
→ Welcome Email
→ Logging

## Run Locally

```bash
uvicorn app.main:app --reload
```

## API Docs

```txt
http://127.0.0.1:8000/docs
```