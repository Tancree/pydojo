from collections import defaultdict
from pydantic import BaseModel

from src.model.game import Game


class Player(BaseModel):
    name: str
    id: str
    scores: defaultdict[Game, int]
    total_score: int

    def __repr__(self) -> str:
        return f"Player name: {self.name}, id: {self.id}, scores: {self.scores}, total_score: {self.total_score}"
