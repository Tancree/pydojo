from src.model.command import Command
from src.model.player import Player


def main():
    print("Hello from pydojo!")

    stay = True
    while stay:
        user_input = input("Enter your command\n")
        command = Command(user_input.split(" ")[0])
        args = user_input.split(" ", 2)[1]
        match command:
            case Command.Close:
                stay = False

            case Command.GetScores:
                print(f"Command is {command}, args {args}")


if __name__ == "__main__":
    players: list[Player] = []
    main()
