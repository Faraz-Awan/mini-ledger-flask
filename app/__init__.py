from flask import Flask
from sqlalchemy import text
from app.db import engine

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app