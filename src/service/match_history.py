from src.model.match_history import Match


def add_match() -> Match:
    game = input("Enter the game name:\n")
    team1 = input("Enter team 1 players (comma separated):\n")
    team2 = input("Enter team 2 players (comma separated):\n")
    team1 = team1.split(",")
    team2 = team2.split(",")
    winner = input("Enter the winner team (team1/team2):\n")
    return Match(
        game=game,
        teams=[team1, team2],
        winner=team1 if winner == "team1" else team2,
    )
