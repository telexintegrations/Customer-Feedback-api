from flask import Blueprint, jsonify
from flask_cors import CORS
from app.config import Config
import os

telex_bp = Blueprint("telex", __name__)
CORS(telex_bp)
@telex_bp.route("/telex_settings", methods=["GET"])
def telex_settings():
    """Return the Telex integration JSON settings."""
    settings = {
  "data": {
    "date": {
      "created_at": "2025-02-19",
      "updated_at": "2025-02-21"
    },
    "descriptions": {
      "app_name": "Customer-Feedback-Api",
      "app_description": "This customer-feedback interval integration gathers customer complaints and reviews in regard to a business or product.",
      "app_logo": "https://imgur.com/a/fXIRcLD",
      "app_url": "https://customer-feedback-api-ckii.onrender.com/all?token=9cy2u2VF5pVxYKxcHOl8",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "interval",
    "integration_category": "CRM & Customer Support",
    "key_features": [
      "Real-Time Data of all logged complaints/reviews"
    ],
    "author": "Emarve",
    "settings": [
      {
        "label": "interval",
        "type": "text",
        "required": True,
        "default": "* * * * *"
      }
    ],
    "target_url": "https://ping.telex.im/v1/webhooks/01951578-b933-7f1a-a6db-9984ac50486f",
    "tick_url": "https://customer-feedback-api-ckii.onrender.com/all?token=9cy2u2VF5pVxYKxcHOl8"
  }
}
    return jsonify(settings)