from datetime import datetime
from pydantic import BaseModel

from src.model.game import Game
from src.model.player import Player


class Match(BaseModel):
    game: str
    teams: list[list[str]]  # string palyers names
    winner: list[str]  # string players names

    def __str__(self):
        teams_str = ""
        i = 0
        for team in self.teams:
            teams_str += f"Team {i + 1}: {', '.join(team)}  "
            i += 1
        return f"{self.game} - teams. {teams_str} - winner: {', '.join(self.winner)}"
