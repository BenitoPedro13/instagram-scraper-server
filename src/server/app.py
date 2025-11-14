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
    return app

# Expose a module-level app so tests and WSGI servers can import it easily.
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
