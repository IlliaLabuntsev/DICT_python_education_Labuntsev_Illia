"""TicTacToe Project"""
import sys


def draw_field(board):
    """Function draw_field: This function prints a board for the tic tac toe game

       Parameters:
       str(board): tic tac toe game board

       Returns:
       str(board): returns tic tac toe game board
    """
    print("---------" + "\n" + "| " + " ".join(board[:3]) + " |"
          + "\n" + "| " + " ".join(board[3:6]) + " |"
          + "\n" + "| " + " ".join(board[6:9]) + " |" + "\n" + "---------")


def analyze_state(board):
    """Function analyze_state: This function analyzing tic tac toe game board

        Parameters:
        str(board): tic tac toe game board

        Returns:
        str x_wins: returns win for X player
        str o_wins: returns win for O player
        empty str: if "_" in game board
        str "Draw": if no one wins this game
    """
    x_wins = o_wins = False

    # Check for a win
    for i in range(0, 3):
        # Check rows and columns
        if board[i] == board[i + 3] == board[i + 6] != '_':
            if board[i] == 'X':
                x_wins = True
            else:
                o_wins = True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != '_':
            if board[i * 3] == 'X':
                x_wins = True
            else:
                o_wins = True

    # Check diagonals
    if board[0] == board[4] == board[8] != '_':
        if board[0] == 'X':
            x_wins = True
        else:
            o_wins = True
    if board[2] == board[4] == board[6] != '_':
        if board[2] == 'X':
            x_wins = True
        else:
            o_wins = True

    # Check for Impossible
    if (x_wins and o_wins) or (board.count('X') - board.count('O')) > 1 or (board.count('O') - board.count('X')) > 1:
        print("Impossible")
        sys.exit()

    """ 
        Check for a draw or game not finished 
        if X wins program will return the message "X wins"
        if O wins program will return the message "O wins"
        if "_" is in board program will return an empty string and continue working
        if X or O don't win and if "_" is not in the board, the program returns "Draw"
    """
    if x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' in board:
        return ""
    else:
        return "Draw"


def play_tic_tac_toe():
    """Function play_tic_tac_toe: This function initializes an empty board list and calls the function draw_field and analyze_state

       Parameters:
       -

       Returns:
       -
    """
    # Get initial input for the game board
    board = list("_________")  # Initial empty board
    draw_field(board)
    current_player = 'X'

    # Main game loop
    while True:
        try:
            # Get user input for the move coordinates
            coordinates = input("Enter the coordinates: ")
            row, col = map(int, coordinates.split())

            # Check if coordinates are within the valid range
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Coordinates must be from 1 to 3! Try again.")
                continue

            # Calculate the index in the board list based on the coordinates
            index = (row - 1) * 3 + (col - 1)

            # Check if the chosen cell is empty
            if board[index] == '_':
                # Update the board with the current player's move
                board[index] = current_player
                draw_field(board)  # Draw the updated board
                game_state = analyze_state(board)  # Analyze the state of the game
                print(game_state)  # Print the game state

                # Check if the game is over
                if game_state in ["X wins", "O wins", "Draw"]:
                    return  # Exit the function, which will end the program

                # Switch player for the next move
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This cell is occupied! Choose another one.")

        except ValueError:
            print("You should enter numbers!")


# Start the game
play_tic_tac_toe()
