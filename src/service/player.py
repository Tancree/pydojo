from collections import defaultdict
from uuid import uuid4

from src.model.player import Player


def new_player(name) -> Player:
    """"""
    return Player(
        name=name,
        id=str(uuid4()),
        scores=defaultdict(int),
        total_score=0,
    )
