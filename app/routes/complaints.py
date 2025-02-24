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
        try:
            response = requests.post(WEBHOOK_URL)
        except requests.exceptions.RequestException as e:
            print(f"Error sending webhook: {e}")
            return jsonify({"error": "Complaint is required"}), 400
        add_complaint(name, complaint)
        return jsonify({"message": "Complaint submitted successfully"}), 201
    return render_template("index.html")

@complaints_bp.route("/all", methods=["GET"])
def get_complaints():
     complaints = get_all_complaints()
     return jsonify([{ 
         "id": c.id, 
         "name": c.name, 
         "complaint": c.complaint, 
         "created_at": c.created_at } 
         for c in complaints])
