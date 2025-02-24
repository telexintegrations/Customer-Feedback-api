from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os

db = SQLAlchemy()

def create_app():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get absolute path
    templates_path = os.path.join(BASE_DIR, "/Customer-Feedback-api/templates")   # Correct path

    app = Flask(__name__, template_folder=templates_path)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        from app.routes.complaints import complaints_bp
        from app.routes.telex import telex_bp
        app.register_blueprint(complaints_bp)
        app.register_blueprint(telex_bp, url_prefix="/api/v1/telex")
        
        db.create_all()  # Create database tables
    
    return app