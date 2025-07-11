from collections import defaultdict
from uuid import uuid4

from src.model.player import Player
from src.data import players, games


def new_player(name) -> Player:
    """"""
    return Player(
        name=name,
        id=str(uuid4()),
        scores=defaultdict(int),
        total_score=0,
    )


def print_scores(game):
    if game not in [g.name for g in games]:
        print(f"this game does not exists: {[g.name for g in games]}")
    else:
        ranking = sorted(players, key=lambda player: player.scores[game], reverse=True)
        print(f"Here the ranking for game {game}")
        for i, player in enumerate(ranking):
            print(f"    {i + 1}) {player.name} {player.scores[game]} points")
