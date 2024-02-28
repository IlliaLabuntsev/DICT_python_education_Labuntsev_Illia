"""Pencils game project"""
import random


def get_pencils():
    """
        Function get_pencils: This function requests amount of pencils from the user
        Parameters:
        None

        Returns:
        int(pencil): returns the value of pencils that are used in the game
    """
    while True:
        try:
            pencil = int(input("How many pencils would you like to use: \n"))
            if pencil > 0:
                return pencil
            elif pencil == 0:
                print("The number of pencils should be positive.")
            else:
                print("The number of pencils should be numeric.")
        except ValueError:
            print("The number of pencils should be numeric")


def choose_first():
    """
        Function choose_first: This function requests name of the first player
        Parameters:
        None

        Returns:
        str(player): returns the name of the first player in the game
    """
    while True:
        player = input(f"Who will be the first ({name_first}, {name_second}): ")

        if player == name_first:
            print("|" * pencils)
            print(f"{name_first} is going first")
            return player
        elif player == name_second:
            print("|" * pencils)
            print(f"{name_second} is going first")
            return player
        else:
            print(f"Choose between '{name_first}' and '{name_second}'")


def game_starts(amount_of_pencils, first_player_in_game):
    """
        Function game_starts: This function shows who is currently making a move,
        checks that the number of pencils is not more than 3, after entering the number of pencils,
        after which it calculates how many pencils are left and displays the remaining number in the console
        Parameters:
        int(amount_of_pencils): Receive the amount of pencils that are used in the game.
        str(first_player_in_game): Receive the name of the first player.

        Returns:
        None
    """

    while amount_of_pencils > 0:
        current_player = first_player_in_game
        print(f"{current_player}'s turn:")

        if current_player == name_first:
            pencils_to_pick = input()
            try:
                pencils_to_pick = int(pencils_to_pick)
                if 1 <= pencils_to_pick <= 3 and pencils_to_pick <= amount_of_pencils:
                    amount_of_pencils -= pencils_to_pick
                    print("|" * amount_of_pencils)
                    first_player_in_game = name_second
                elif pencils_to_pick > amount_of_pencils:
                    print("Too many pencils were taken.")
                elif pencils_to_pick <= 0:
                    print("Possible values: '1', '2' or '3'")
                else:
                    print("Possible values: '1', '2' or '3'")
            except ValueError:
                print("Please enter a number!")

        else:  # Bot's move
            bot_pencils_to_pick = bot_move(amount_of_pencils)
            amount_of_pencils = bot_pencils_to_pick
            print("|" * amount_of_pencils)
            first_player_in_game = name_first

    print(f"{first_player_in_game} winner!")


def bot_move(pencil):
    """
        Function bot_move: This function calculates bot move
        Parameters:
        int(pencils): requests the value of pencils that are left

        Returns:
        int(pencil): value of pencils that are left after bot move
    """
    if pencil == 1:
        take = 1
    elif pencil % 4 == 1:
        take = random.randint(1, min(3, pencil))
    else:
        take = (pencil - 1) % 4

    pencil -= take
    print(f"{name_second} takes {take} pencil(s)")
    print(f"Bot chose {take} pencil(s)")
    return pencil


pencils = get_pencils()  # Get amount of pencils
name_first = input("Enter name of the first player: \n")  # Get the first player name
bot_random_name = ['Alex', 'Ivan', 'Artem', 'Dmitry']
name_second = random.choice(bot_random_name)  # Get the second player name
first_player = choose_first()  # Choose the first

# Call functions
game_starts(pencils, first_player)
