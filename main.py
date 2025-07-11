from src.model.command import Command
from src.model.player import Player
from src.service import player as player_service
from src.service.game import new_game

def main():
    print("Hello from pydojo!")

    stay = True
    while stay:
        user_input = input("\nEnter your command\n")
        command = Command(user_input.split(" ")[0])
        user_input_split = user_input.split(" ", 1)
        if len(user_input_split) > 1:
            args = user_input.split(" ", 1)[1]
        else:
            args = None
        match command:
            case Command.Close:
                stay = False

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
                new_game = new_game(args)
                

            case Command.GetPlayers:
                # get_players
                print("Players are:")
                for player in players:
                    print(f"    {player}")
            case _:
                print("Unknown command, please retry")




if __name__ == "__main__":
    players: list[Player] = []
    main()
