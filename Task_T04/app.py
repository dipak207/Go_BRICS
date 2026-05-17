from flask import Flask, request, jsonify
import requests
import logging
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
# Logging setup
logging.basicConfig(
    filename='integration.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Home route
@app.route('/')
def home():
    return "Flask API Integration Running Successfully"


# Main API endpoint
@app.route('/submit', methods=['POST'])
def submit():

    try:
        # Get JSON data
        data = request.json

        # Validate request body
        if not data:
            logging.error("No JSON payload received")

            return jsonify({
                "status": "error",
                "message": "No JSON data received"
            }), 400

        # Validate email field
        if not data.get("email"):

            logging.error("Submission failed: Email missing")

            return jsonify({
                "status": "error",
                "message": "Email is required"
            }), 400

        # Create Slack message
        message = {
            "text": f"""
New Submission Received

Name: {data.get('name')}
Email: {data.get('email')}
Message: {data.get('message')}
"""
        }

        # Send message to Slack
        response = requests.post(
            SLACK_WEBHOOK,
            json=message
        )

        # Debugging output
        print("Slack Response Code:", response.status_code)
        print("Slack Response Text:", response.text)

        # Check Slack API response
        if response.status_code != 200:

            logging.error(f"Slack API Error: {response.text}")

            return jsonify({
                "status": "error",
                "message": f"Slack API Error: {response.text}"
            }), 500

        # Success log
        logging.info(f"Submission successful: {data}")

        # Success response
        return jsonify({
            "status": "success",
            "message": "Data sent to Slack successfully"
        })

    except Exception as e:

        print("SYSTEM ERROR:", str(e))

        logging.error(f"System error: {str(e)}")

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)