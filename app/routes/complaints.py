from flask import Blueprint, request, jsonify, render_template
from app.services.complaint_service import add_complaint, get_all_complaints
import requests

complaints_bp = Blueprint("complaints", __name__)
WEBHOOK_URL = 'https://ping.telex.im/v1/webhooks/01951578-b933-7f1a-a6db-9984ac50486f'

@complaints_bp.route("/", methods=["GET", "POST"])
def submit_complaint():
    if request.method == "POST":
        name = request.form.get("name")
        complaint = request.form.get("complaint")

        # Validate that the complaint is provided
        if not complaint:
            return jsonify({"error": "Complaint is required"}), 400

        # Add the complaint to the database
        new_complaint = add_complaint(name, complaint)

        # Prepare the payload for the Telex webhook
        payload = {
            "event_name": "new_complaint",
            "message": f"New Complaint Received:\nID: {new_complaint.id}\nName: {name}\nComplaint: {complaint}",
            "status": "success",
            "username": "complaint_bot"  # Replace with your desired username
        }

        # Send the payload to the Telex webhook
        try:
            response = requests.post(
                WEBHOOK_URL,
                json=payload,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()  # Raise an error for bad status codes
            print("Notification sent successfully:", response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error sending webhook: {e}")
            return jsonify({"error": "Failed to send notification"}), 500

        return jsonify({"message": "Complaint submitted successfully"}), 201

    return render_template("index.html")

@complaints_bp.route("/all", methods=["GET"])
def get_complaints():
    complaints = get_all_complaints()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "complaint": c.complaint,
        "created_at": c.created_at
    } for c in complaints])
    