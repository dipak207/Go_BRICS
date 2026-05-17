# TASK_T04 — API Integration Documentation

## Project Title

Flask to Slack API Integration System

---

# 1. Project Overview

This project demonstrates a working API integration between a Python Flask application and Slack using Slack Incoming Webhooks.

The system receives user submission data through an API endpoint and automatically sends formatted notifications to a Slack channel.

The integration also includes:

* Input validation
* Error handling
* Activity logging
* Monitoring support
* API testing through Postman

This project was developed to satisfy the TASK_T04 requirement:

> Test a functional integration between two platforms using APIs.

---

# 2. Platforms Integrated

| Platform         | Purpose                          |
| ---------------- | -------------------------------- |
| Python Flask API | Receives and processes user data |
| Slack            | Receives automated notifications |

---

# 3. Integration Workflow

## System Flow

1. User sends data to the Flask API endpoint.
2. Flask validates the incoming data.
3. If validation passes:

   * Data is formatted into a message.
   * Message is sent to Slack using Slack Webhooks.
4. If validation fails:

   * Error response is returned.
   * Error is logged in the monitoring log file.
5. All successful and failed requests are stored in logs.

---

# 4. Technologies Used

| Technology              | Purpose                          |
| ----------------------- | -------------------------------- |
| Python                  | Backend programming language     |
| Flask                   | API framework                    |
| Requests Library        | Sending HTTP requests            |
| Slack Incoming Webhooks | Slack API integration            |
| Postman                 | API testing                      |
| Logging Module          | Monitoring and activity tracking |

---

# 5. Folder Structure

```
TASK_T04/
│
├── app.py
├── run.bat
├── requirements.txt
├── documentation.md
├── integration.log
├── screenshots/
└── README.md
```

---

# 6. File Descriptions

| File             | Purpose                               |
| ---------------- | ------------------------------------- |
| app.py           | Main Flask application                |
| run.bat          | Starts the Flask server automatically |
| requirements.txt | Lists required Python libraries       |
| documentation.md | Project documentation                 |
| integration.log  | Stores activity and error logs        |
| screenshots/     | Contains proof screenshots            |
| README.md        | GitHub project overview               |

---

# 7. How to Run the System

## Step 1 — Install Python

Install Python from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Step 2 — Install Required Libraries

Open terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

This installs:

* Flask
* Requests

---

## Step 3 — Start the Application

Double-click:

```
run.bat
```

OR manually run:

```bash
python app.py
```

---

## Step 4 — Verify Application is Running

If successful, terminal displays:

```text
Running on http://127.0.0.1:5000
```

This means the API is active.

---

# 8. API Endpoint Information

| Endpoint | Method | Purpose                  |
| -------- | ------ | ------------------------ |
| /submit  | POST   | Receives submission data |

Full local endpoint:

```text
http://127.0.0.1:5000/submit
```

---

# 9. Testing the Integration

## Using Postman

### Step 1

Open Postman.

### Step 2

Create a new POST request.

### Step 3

Enter URL:

```text
http://127.0.0.1:5000/submit
```

### Step 4

Select:

* Body
* raw
* JSON

### Step 5

Paste sample JSON:

```json
{
  "name": "Dipak Gupta",
  "email": "dipak@gmail.com",
  "message": "Testing API integration"
}
```

### Step 6

Click Send.

---

# 10. Expected Successful Output

## API Response

```json
{
  "status": "success",
  "message": "Data sent to Slack successfully"
}
```

---

## Slack Notification

Slack channel receives:

```text
New Submission Received

Name: Dipak Gupta
Email: dipak@gmail.com
Message: Testing API integration
```

---

# 11. Error Handling

The integration includes validation and monitoring for incorrect input.

---

## Error Case Example

If email field is missing:

```json
{
  "name": "Dipak Gupta",
  "message": "Testing error handling"
}
```

---

## Expected Error Response

```json
{
  "status": "error",
  "message": "Email is required"
}
```

---

## What Happens Internally

* Request is rejected.
* Error response returned.
* Error written to integration.log.
* Slack message is NOT sent.

---

# 12. Monitoring and Logs

All activities are automatically stored in:

```text
integration.log
```

---

## Successful Log Example

```text
INFO Submission successful
```

---

## Error Log Example

```text
ERROR Submission failed: Email missing
```

---

# 13. How to Check if the System Breaks

The system should be checked using the following methods:

## Method 1 — Terminal Output

Check Flask terminal window for:

* HTTP 200 = successful requests
* HTTP 400 = validation errors
* HTTP 500 = system/server errors

---

## Method 2 — integration.log

Open:

```text
integration.log
```

Look for:

* ERROR messages
* Missing requests
* Slack API failures

---

## Method 3 — Slack Channel

If Slack notifications stop appearing:

Possible causes:

* Invalid webhook URL
* Internet connection failure
* Flask server not running
* Slack webhook disabled

---

# 14. Troubleshooting Guide

| Problem            | Possible Cause                   | Solution              |
| ------------------ | -------------------------------- | --------------------- |
| 404 Error          | Wrong endpoint                   | Use /submit endpoint  |
| 405 Error          | GET request used instead of POST | Use POST method       |
| 500 Error          | Internal server error            | Check integration.log |
| No Slack Message   | Invalid webhook                  | Regenerate webhook    |
| Connection Refused | Flask server stopped             | Restart app.py        |

---

# 15. Security Notes

* Slack webhook URL should not be shared publicly.
* Webhook should be regenerated if exposed.
* Sensitive credentials should ideally be stored in environment variables.

---

# 16. Future Improvements

Possible future enhancements:

* Database storage
* Email notifications
* Public cloud deployment
* Authentication system
* Dashboard for monitoring
* Docker deployment

---

# 17. Project Outcome

This integration successfully demonstrates:

* API communication
* Real-time data transfer
* Error handling
* Monitoring and logging
* Slack automation
* Functional system integration
The project fulfills the TASK_T04 requirement for a tested and documented API integration.
