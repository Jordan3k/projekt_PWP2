import os

from flask import Flask
from app.config import Config
from app.db import db
from typing import Optional, List, Dict, Any

def create_app(config: Optional[Config] = None) -> Flask:
    app = Flask(__name__)


    cfg = config or Config.from_env()
    app.config.update(
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "postgresql://postgres:WertyCV78!@localhost:5432/flaskToDo"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY=cfg.secret_key,
    )


    db.init_app(app)


    # Register routes
    from .app import bp as app_bp # noqa: WPS433 (import inside function)


    app.register_blueprint(app_bp)


    # Create tables if not present (for demo/dev)
    with app.app_context():
        db.create_all()


    return app