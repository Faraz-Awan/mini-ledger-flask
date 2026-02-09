from flask import Flask
from sqlalchemy import text
from app.db import engine

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))

def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app