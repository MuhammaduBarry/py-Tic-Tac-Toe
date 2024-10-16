# Import python module
import pyfiglet
from termcolor import colored

# Initialize the tic-tac-toe board in a function to reset between rounds
def create_board():
    return [
        ['0', '1', '2'],
        ['3', '4', '5'],
        ['6', '7', '8']
]

# Initialize the main board to be reset after each round
tic_tac_toe_board = create_board()

def get_main_board():
    """Creates the main board every time it is called"""
    main_board = f'''
        {tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}
        --|---|--
        {tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]}
        --|---|--
        {tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}
        '''
    return main_board

def intro():
    """Define Rules and Information needed to play"""

    # Create ASCII art
    intro_ascii_art = colored(pyfiglet.figlet_format('''Welcome to Tic-Tac-Toe''', font = "larry3d", width = 135, justify = "right"), color = "cyan")

    # Instructions
    intro_statement = f'''
    The rules are simple:
    {get_main_board()}
    This is a turn based program, The first player that will start is the first player who inputs their name and symbol.

    1. After players and symbols have been selected, player 1 will choose a number between 0-8.
    2. Then player 2 will choose another number 0-8, until the players get three in a row, column, and diagonal.
    3. You will be prompted on how many games you would like to play, 1 up to 5.
    4. Make sure you double check if the space number has been taken before inputting your number.
    5. Good luck and have fun :)
    '''

    # Introduction print statement
    print(f"\n{intro_ascii_art}")
    print(intro_statement)

def display_current_board(input, player_symbol):
    """Function to display and track player game"""
    if input <= 2:
        tic_tac_toe_board[0][input] = player_symbol
    elif 2 < input <= 5:
        tic_tac_toe_board[1][input - 3] = player_symbol
    elif 5 < input <= 8:
        tic_tac_toe_board[2][input - 6] = player_symbol
    else:
        print("Index out of bound won't work")

    print(get_main_board())

def check_win(player_name):
    x_list = ["x", "x", "x"]
    o_list = ["o", "o", "o"]

    win_conditions = [
        [tic_tac_toe_board[0][0], tic_tac_toe_board[1][0], tic_tac_toe_board[2][0]],
        [tic_tac_toe_board[0][1], tic_tac_toe_board[1][1], tic_tac_toe_board[2][1]],
        [tic_tac_toe_board[0][2], tic_tac_toe_board[1][2], tic_tac_toe_board[2][2]],
        [tic_tac_toe_board[0][0], tic_tac_toe_board[0][1], tic_tac_toe_board[0][2]],
        [tic_tac_toe_board[1][0], tic_tac_toe_board[1][1], tic_tac_toe_board[1][2]],
        [tic_tac_toe_board[2][0], tic_tac_toe_board[2][1], tic_tac_toe_board[2][2]],
        [tic_tac_toe_board[0][0], tic_tac_toe_board[1][1], tic_tac_toe_board[2][2]],
        [tic_tac_toe_board[0][2], tic_tac_toe_board[1][1], tic_tac_toe_board[2][0]],
    ]

    for condition in win_conditions:
        if condition == x_list or condition == o_list:
            print(f"\n{player_name} has won!!!")
            return True
    return False

def reset_game():
    """Reset the board and other variables for a new round"""
    global tic_tac_toe_board
    tic_tac_toe_board = create_board()

def game_logic():
    """Create logic that will house the core program functionality"""

    while True:
        game_rounds = input("\nHow many rounds would you like to play? ")
        if game_rounds.isdigit() and 1 <= int(game_rounds) <= 5:
            game_rounds = int(game_rounds)
            break
        else:
            print("Only number between 1 and 5 are allowed try again!")
    
    player_one = input("\nWhat is your name Player one: ")

    while True:
        player_one_symbol = input("\nWhat symbol would you like to use x or o?: ").lower()
        if player_one_symbol in ["x", "o"]:
            break
        else:
            print("Player symbol has to either 'x' or 'o'")

    player_two = input("\nWhat is your name Player two: ")
    
    if player_one_symbol == "x":
        player_two_symbol = "o"
    else:
        player_two_symbol = "x"

    current_round = 1
    player_one_wins = 0
    player_two_wins = 0

    while current_round <= game_rounds:
        print(f"\nRound {current_round} starts now!")

        spots_available = list(range(0, 9))
        def player_move(player_name, player_symbol):
            while True:
                move_input = input(f"\nPick an available spot {player_name}: ")
                if move_input.isdigit():
                    move_input = int(move_input)
                    if move_input in spots_available:
                        display_current_board(move_input, player_symbol)
                        spots_available.remove(move_input)
                        break
                    else:
                        print("Spot already taken or invalid. Try again.")
                else:
                    print("Numbers 0-8 only.")

        is_player_one_turn = True
        winner = None
        while spots_available:
            if is_player_one_turn:
                player_move(player_one, player_one_symbol)
                if check_win(player_one):
                    player_one_wins += 1
                    winner = player_one
                    break
                is_player_one_turn = False
            else:
                player_move(player_two, player_two_symbol)
                if check_win(player_two):
                    player_two_wins += 1
                    winner = player_two
                    break
                is_player_one_turn = True
        
        if not winner:
            print("It's a tie!")
        
        current_round += 1
        reset_game()  # Reset the board for the next round

    print(f"\nFinal Score: {player_one}: {player_one_wins}, {player_two}: {player_two_wins}")
    if player_one_wins > player_two_wins:
        print(f"{player_one} wins the game!")
    elif player_two_wins > player_one_wins:
        print(f"{player_two} wins the game!")
    else:
        print("The game is a tie!")

def main():
    """Function to house and organize program"""
    intro()
    game_logic()

main()
