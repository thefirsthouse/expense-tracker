"""Expense model file"""

from typing import Optional
from dataclasses import asdict


class Expense:
    """Basic expense model"""

    id: int
    description: str
    amount: float
    date: Optional[str] = None


    def to_dict(self) -> dict:
        """Moves Expense object into dict"""
        return asdict(self)
    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            date=data["date"]
        )
