from collections import defaultdict
from pydantic import BaseModel

from src.model.games import Games


class Player(BaseModel):
    name: str
    id: str
    scores: defaultdict[Games, int]
    total_score: int

    def __repr__(self) -> str:
        return f"Player name: {self.name}, id: {self.id}, scores: {self.scores}, total_score: {self.total_score}"
