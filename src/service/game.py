from src.model.game import Game
from src.model.match_history import Match
from uuid import uuid4
from main import games, match_history

def new_game(name:str) -> Game:
    return Game(name=name,id=str(uuid4()))

def get_games() -> list[Game]:
    return games

def get_game_id(name:str) -> str:
    for game in games:
        if game.name == name:
            return game.id

def get_game(name:str) -> Game:
    for game in games:
        if game.name == name:
            return game

def get_game_match_history(game_name: str) -> list(Match):
    game = get_game(game_name)
    game_match_history = []
    for match in match_history:
        if (match.game == game):
            game_match_history.append(match)
    return game_match_history

