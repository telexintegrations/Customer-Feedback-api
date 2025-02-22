import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "01951578-b933-7f1a-a6db-9984ac50486f")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///complaints.db")
    
    # Telex integration settings
    TELEX_TOKEN = os.environ.get("TELEX_TOKEN", "telex_secret_token")
    TELEX_TARGET_URL = os.environ.get("TELEX_TARGET_URL", "https://ping.telex.im/v1/webhooks/01951578-b933-7f1a-a6db-9984ac50486f")
    TELEX_API_KEY = os.environ.get("TELEX_API_KEY", "9cy2u2VF5pVxYKxcHOl8")
    
    # Application base URL
    APP_BASE_URL = os.environ.get("APP_BASE_URL", "https://customer-feedback-api-ckii.onrender.com/all")