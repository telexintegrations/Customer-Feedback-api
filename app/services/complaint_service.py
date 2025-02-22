from app.models.complaint import Complaint
from app import db

def add_complaint(name, complaint):
    new_complaint = Complaint(name=name, complaint=complaint)
    db.session.add(new_complaint)
    db.session.commit()
    return new_complaint

def get_all_complaints():
    return Complaint.query.all()