from collections import defaultdict
from src.model.game import Game
from src.model.player import Player


players: list[Player] = [
    Player(
        name="a",
        id=str("uuid4()"),
        scores=defaultdict(int),
        total_score=0,
    ),
    Player(
        name="b",
        id=str("a"),
        scores=defaultdict(int),
        total_score=0,
    ),
    Player(
        name="c",
        id=str("a"),
        scores=defaultdict(int),
        total_score=0,
    ),
    Player(
        name="d",
        id=str("a"),
        scores=defaultdict(int),
        total_score=0,
    ),
]
games: list[Game] = [Game(name="game", id=str("uuid4()"))]
match_history = []
