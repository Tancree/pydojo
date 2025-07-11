from src.model.command import Command
from src.model.player import Player
from src.service import player


def main():
    print("Hello from pydojo!")

    stay = True
    while stay:
        user_input = input("Enter your command\n")
        command = Command(user_input.split(" ")[0])
        args = user_input.split(" ", 1)[1]
        match command:
            case Command.Close:
                stay = False

            case Command.GetScores:
                print(f"Command is {command}, args {args}")

            case Command.NewPlayer:
                # new_player NAME
                new_player = player.new_player(args)
                players.append(new_player)
                print(f"Added new player {new_player}")


if __name__ == "__main__":
    players: list[Player] = []
    main()
