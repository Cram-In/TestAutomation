def display_board(board):

    # clear_output()

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")


test_board = [" "] * 10


def player_input():

    marker = ""

    while marker != "X" and marker != "O":

        print("Please select X or O")

        marker = input("Player 1, Please slect your's marker (X, O): ").upper()

    player_1 = marker

    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"

    return (player_1, player_2)


player_1_marker, player_2_marker = player_input()


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    # win tic tack toe?

    # all rows, and check to see if they all mach
    #    (board[1] == mark and board[2] == mark and board[3] mark) or
    #    (board[4] == mark and board[5] == mark and board[6] mark) or
    #    (board[7] == mark and board[8] == mark and board[9] mark) or
    return (
        (board[1] == board[2] == board[3] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[7] == board[8] == board[8] == mark)
        or (board[1] == board[4] == board[7] == mark)
        or (board[2] == board[5] == board[8] == mark)
        or (board[3] == board[6] == board[9] == mark)
        or (board[1] == board[5] == board[9] == mark)
        or (board[7] == board[5] == board[3] == mark)
    )

    # all colums , check for mach
    # 2 diagonals checks


import random


def choose_first():

    if random.randint(0, 1) == 0:

        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):

    return board[position] == " "


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9)"))

    return position


def replay():

    choice = "wrong"

    while choice not in ["Y", "N"]:

        choice = input("Keep playing? (Y or N)").upper()

        if choice not in ["Y", "N"]:
            print("Sorry, invalid choice!, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False


print("Welcome in Tic Tac Toe")

while True:
    # play a game

    the_board = [" "] * 10

    player_1_marker, player_2_marker = player_input()

    turn = choose_first()

    print(turn + " will go first.")

    play_game = input("Ready to play? Y or N? ")

    if play_game.lower()[0] == "y":
        game_on = True
    else:

        game_on = False

    while game_on:

        if turn == "Player 1":
            # show the board

            display_board(the_board)

            print("_____________")
            print("Player 1 turn")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
            # choose position
            position = player_choice(the_board)

            place_marker(the_board, player_1_marker, position)

            if win_check(the_board, player_1_marker):
                display_board(the_board)
                print(" Player 1 Has Won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False

                else:
                    turn = "Player 2"

        else:

            display_board(the_board)
            # choose position
            print("_____________")
            print("Player 2 turn")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾")

            position = player_choice(the_board)

            place_marker(the_board, player_2_marker, position)

            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print(" Player 2 Has Won!!!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False

                else:
                    turn = "Player 1"

    if not replay():
        break