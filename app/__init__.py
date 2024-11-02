from flask import Flask
from app.routes.http_routes import http_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(http_bp)
    return app
