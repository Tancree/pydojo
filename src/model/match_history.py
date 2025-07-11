from datetime import datetime
from pydantic import BaseModel

from src.model.games import Games
from src.model.player import Player


class Match(BaseModel):
    game: Games
    teams: list[list[Player]]
    winner: list[Player]
    date: datetime
