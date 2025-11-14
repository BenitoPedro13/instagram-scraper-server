import os
import sys
from flask import Flask

# Ensure the project root (which contains the src package) is on sys.path.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.server.routes import setup_routes

def create_app():
    app = Flask(__name__)
    setup_routes(app)

    # CORS básico para permitir chamadas de qualquer origem (inclui file:// com origem null)
    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        return response

    return app

# Expose a module-level app so tests and WSGI servers can import it easily.
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")
