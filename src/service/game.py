from src.model.game import Game
from uuid import uuid4

def new_game(name:str) -> Game:
    return Game(name=name,id=str(uuid4()))

def get_games(name:str) -> Game:
    return

