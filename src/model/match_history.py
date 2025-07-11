from datetime import datetime
from pydantic import BaseModel

from src.model.game import Game
from src.model.player import Player


class Match(BaseModel):
    game: Game
    teams: list[list[Player]]
    winner: list[Player]
    date: datetime
