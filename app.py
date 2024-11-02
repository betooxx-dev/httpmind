from flask import Flask, render_template
from app.routes.http_routes import http_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(http_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)