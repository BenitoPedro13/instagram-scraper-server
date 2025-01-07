from flask import Flask
from routes import setup_routes  # Changed from relative import

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)