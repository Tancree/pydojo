from collections import defaultdict
from pydantic import BaseModel

from src.model.games import Games


class Player(BaseModel):
    name: str
    id: str
    scores: defaultdict[Games, int]
    total_score: int
