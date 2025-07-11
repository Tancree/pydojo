from enum import Enum


class Command(Enum):
    new_player = "new_player"
    get_scores = "get_scores"
    new_game = "new_game"
    get_games = "games"
    game_match_history = "game_match_history"
    add_match = "add_match"
    get_match = "get_match"


class GetScoresParams(Enum):
    game: str | None
    player: str | None
