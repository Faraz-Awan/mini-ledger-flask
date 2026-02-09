from flask import Blueprint, request

bp = Blueprint("api", __name__)

@bp.get("/health")
def health_check():
    return {"status": "ok"}

@bp.post("/accounts")
def create_acount():
    payload = request.get_json() or {}
    return {
        "account_name": payload.get("account_name"),
        "user_id": payload.get("user_id"),
        "message": "accounts endpoint skeleton"
    }, 200