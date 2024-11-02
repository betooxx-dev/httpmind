from flask import Blueprint, jsonify, render_template
from app.services.http_service import HttpService
from app.repositories.http_repository import HttpRepository

http_bp = Blueprint('http', __name__)
http_service = HttpService(HttpRepository())

@http_bp.route('/')
def index():
    return render_template('index.html')

@http_bp.route('/api/status/<code>')
def get_status(code):
    status_info = http_service.get_status_info(code)
    if status_info:
        return jsonify(status_info)
    return jsonify({
        "error": "Código no encontrado",
        "message": "El código de estado HTTP especificado no está en nuestra base de datos."
    }), 404

@http_bp.route('/api/status/type/<type_name>')
def get_status_by_type(type_name):
    status_list = http_service.get_status_by_type(type_name)
    return jsonify(status_list)