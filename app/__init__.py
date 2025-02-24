from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="Customer-Feedback-api/templates")
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