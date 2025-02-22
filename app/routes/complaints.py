from flask import Blueprint, request, jsonify, render_template
from app.services.complaint_service import add_complaint, get_all_complaints

complaints_bp = Blueprint("complaints", __name__)

@complaints_bp.route("/", methods=["GET", "POST"])
def submit_complaint():
    if request.method == "POST":
        name = request.form.get("name")
        complaint = request.form.get("complaint")
        if not complaint:
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
        "created_at": c.created_at
    } for c in complaints])