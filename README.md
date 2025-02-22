# Customer Feedback API

A Flask-based API for collecting and managing customer complaints and reviews. This application integrates with **Telex** to provide real-time updates on customer feedback.

## Features
- Submit customer complaints/reviews via a web form.
- Fetch all complaints in JSON format.
- Telex integration for real-time updates.
- Secure endpoints with API keys and tokens.

## Project Structure
complaint-monitor/
├── app/
│ ├── init.py
│ ├── routes/
│ │ └── complaints.py
│ ├── services/
│ │ └── complaint_service.py
│ └── config.py
│ ├── models/
│   └── complaint.py
├── templates/
│ └── index.html
├── requirements.txt
├── .env
├── wsgi.py
└── README.md


## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/VirusEmp/customer-feedback-api.git
cd customer-feedback-api

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the application
python wsgi.py

API Endpoints
1. Submit a Complaint
URL: /

Method: POST

Description: Submit a customer complaint/review.

Form Fields:

name (optional): Customer name.

complaint (required): Complaint/review text.

2. Fetch All Complaints
URL: /all

Method: GET

Description: Fetch all submitted complaints in JSON format.

3. Telex Integration
URL: /complaints_data

Method: GET

Description: Fetch complaints data for Telex integration.

Query Parameter(token): Telex secret token. #which is gotten after integrating app with telex 

4. Telex Settings
URL: /telex_settings

Method: GET

Description: Fetch Telex integration settings in JSON format.

Telex Integration
This application integrates with Telex to provide real-time updates on customer complaints. The integration includes:

Tick URL: Fetches complaints data at regular intervals.

Target URL: Sends formatted data to Telex's webhook.
