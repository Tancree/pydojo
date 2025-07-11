from src.model.command import Command
from src.model.player import Player
from src.model.game import Game
from src.service import player as player_service
from src.service import game as game_service
from src.model.match_history import Match

players: list[Player] = []
games: list[Game] = []
match_history = []

def main():
    print("Hello from pydojo!")

    stay = True
    while stay:
        user_input = input("\nEnter your command\n")
        try:
            command = Command(user_input.split(" ")[0])
            user_input_split = user_input.split(" ", 1)
            if len(user_input_split) > 1:
                args = user_input.split(" ", 1)[1]
            else:
                args = None
            match command:
                case Command.Close:
                    stay = False
                    print("oh, that was sad... bye bye")

                case Command.AddMatch:
                    game = input("Enter the game name:\n")
                    team1 = input("Enter team 1 players (comma separated):\n")
                    team2 = input("Enter team 2 players (comma separated):\n")
                    team1 = team1.split(",")
                    team2 = team2.split(",")
                    winner = input("Enter the winner team (team1/team2):\n")
                    match_history.append(
                        Match(
                            game=game,
                            teams=[team1, team2],
                            winner=team1 if winner == "team1" else team2,
                        )
                    )

                    # update scores

                case Command.GameMatchHistory:
                    print("Match history:")
                    print("\n".join(str(match) for match in match_history))

                case Command.GetScores:
                    print(f"Command is {command}, args {args}")

                case Command.NewPlayer:
                    # new_player NAME
                    if args is None:
                        print("Hey, I need the player name!")
                    else:
                        new_player = player_service.new_player(args)
                        players.append(new_player)
                        print(f"Added new player {new_player}")
                case Command.NewGame:
                    if args is None:
                        print("Hey, I need the game name!")
                    else:
                        new_game = game_service.new_game(args)
                        games.append(new_game)
                        print(f"Added new game {new_game}")

                case Command.GetPlayers:
                    # get_players
                    print("Players are:")
                    for player in players:
                        print(f"    {player}")
                case _:
                    print("Unknown command, please retry")
        except ValueError:
            print("Ops, this is a wrong command.")


if __name__ == "__main__":
    main()
