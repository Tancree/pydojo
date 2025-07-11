from src.model.match_history import Match

from src.data import players, match_history, games


def update_scores(winning_team: list[str], loosing_team: list[str], game: str) -> None:
    """Update scores for the winning team."""
    for player in winning_team:
        for p in players:
            if p.name == player:
                p.scores[game] += 1

    for player in loosing_team:
        for p in players:
            if p.name == player:
                p.scores[game] += -1


def add_match() -> Match:
    game = input("Enter the game name:\n")
    if game not in [g.name for g in games]:
        print(f"Game {game} not found. Please add it first.")
        return None
    team1 = input("Enter team 1 players (comma separated):\n")
    for player in team1.split(","):
        if player.strip() not in [p.name for p in players]:
            print(f"Player {player.strip()} not found. Please add them first.")
            return None
    team2 = input("Enter team 2 players (comma separated):\n")
    for player in team2.split(","):
        if player.strip() not in [p.name for p in players]:
            print(f"Player {player.strip()} not found. Please add them first.")
            return None
    team1 = team1.split(",")
    team2 = team2.split(",")
    winner = input("Enter the winner team (team1/team2):\n")
    if winner not in ["team1", "team2"]:
        print("Invalid winner. Please enter 'team1' or 'team2'.")
        return None
    update_scores(
        winning_team=team1 if winner == "team1" else team2,
        loosing_team=team2 if winner == "team1" else team1,
        game=game,
    )

    return Match(
        game=game,
        teams=[team1, team2],
        winner=team1 if winner == "team1" else team2,
    )
