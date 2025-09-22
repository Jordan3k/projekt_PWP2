
from dataclasses import dataclass
from datetime import datetime
from app.db import db




@dataclass
class CalculationResult(db.Model): # type: ignore[misc]
    """ORM model for saved calculator results."""


    id: int = db.Column(db.Integer, primary_key=True)
    expression: str = db.Column(db.String(255), nullable=False)
    result: str = db.Column(db.String(255), nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, index=True)


    def __repr__(self) -> str: # pragma: no cover - debug helper
        return f"<Result {self.expression} = {self.result}>"