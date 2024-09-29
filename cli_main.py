import os
import games
import utils.deck

def main():
    _files = os.listdir('./games/')
    files = []
    for file in _files:
        if file == "__init__.py" or file == "__pycache__":
            continue
        else:
            files.append(file)

    print("Wanna play a game?")
    if len(files) == 0:
        print("We need to add some games first...")
    else:
        for index,file in enumerate(files):
            print(f"{index + 1}. {file}")

        game_choice = input("What game would you like to play?\nChoose a number: ")
        game = files[int(game_choice) - 1]
        os.system(f"python {game}")


if __name__ == "__main__":
    main()
