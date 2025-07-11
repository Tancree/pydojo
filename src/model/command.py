from enum import Enum


class Command(Enum):
    Close = "close"
    NewPlayer = "new_player"
    GetPlayers = "get_players"
    GetScores = "get_scores"
    NewGame = "new_game"
    GetGames = "games"
    GameMatchHistory = "game_match_history"
    AddMatch = "add_match"
    GetMatch = "get_match"


class GetScoresParams(Enum):
    game: str | None
    player: str | None


# get_scores --game fifa --player ale
