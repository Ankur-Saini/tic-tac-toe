import random

def display_board(board_list):
    print("     |     |     ")
    print(f"  {board_list[1]}  |  {board_list[2]}  |  {board_list[3]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board_list[4]}  |  {board_list[5]}  |  {board_list[6]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board_list[7]}  |  {board_list[8]}  |  {board_list[9]}  ")
    print("     |     |     ")

def choose_marker():
    marker = ""
    while marker.upper() not in ("X","O"):
        marker = input("Player 1: Choose 'X' or 'O': ")
        if marker.upper() not in ("X","O"):
            print("Invalid input! Choose either 'X' or 'O'")
        else:
            return marker.upper()

def first_turn():
    return random.randint(1,2)

def user_choice(board_list,marker):
    choice = 0
    values = [str(x) for x  in range(1,10)]
    while choice not in values:
        choice = input("Enter your place: ")
        if choice not in values:
            print("Invalid input! Enter a number between 1 to 9.")
        else:
            if board_list[int(choice)] != " ":
                print("Position already taken. Choose another position.")
                choice = 0
            else:
                board_list[int(choice)] = marker

def check_win(board_list,marker):
    if ((board_list[1] == board_list[2] == board_list[3] == marker) or (board_list[4] == board_list[5] == board_list[6] == marker) or (board_list[7] == board_list[8] == board_list[9] == marker) or (board_list[1] == board_list[5] == board_list[9] == marker) or (board_list[3] == board_list[5] == board_list[7] == marker) or (board_list[1] == board_list[4] == board_list[7] == marker) or (board_list[2] == board_list[5] == board_list[8] == marker) or (board_list[3] == board_list[6] == board_list[9] == marker)):
        return True
    else:
        return False

def play_game():
    game = ""
    while game.lower() not in ("yes","no","y","n"):
        game = input("Would you like to play Tic-Tac-Toe? 'yes' or 'no': ")
        if game.lower() not in ("yes","no","y","n"):
            print("Invalid input! Choose 'yes' or 'no'")
    if game.lower() == "yes" or game.lower() == "y":
        return True
    else:
        return False

game = play_game()

while game:
    print("Welcome to Tic-Tac-Toe!")
    board = [" "]*10
    win = False
    marker_1 = choose_marker()
    if marker_1 == 'X':
        marker_2 = 'O'
    else:
        marker_2 = 'X'
    display_board(board)
    print(f"Player 1: {marker_1}\nPlayer 2: {marker_2}")
    turn = first_turn()
    while not win:
        if turn == 1:
            print(f"Player 1's turn: {marker_1}")
            user_choice(board,marker_1)
            turn = 2
            display_board(board)
            win = check_win(board,marker_1)
            if win:
                print("Congrats Player 1! You won the game")
                print("Would you like play Tic-Tac-Toe again?")
                game = play_game()
                if not game:
                    print("Thanks for playing Tic-Tac-Toe!")
                break
        else:
            print(f"Player 2's turn: {marker_2}")
            user_choice(board,marker_2)
            turn = 1
            display_board(board)
            win = check_win(board,marker_2)
            if win:
                display_board(board)
                print("Congrats Player 2! You won the game")
                print("Would you like play Tic-Tac-Toe again?")
                game = play_game()
                if not game:
                    print("Thanks for playing Tic-Tac-Toe!")
                break
        if " " not in board[1:]:
            print("It's a draw between Player 1 and Player 2!")
            print("Would you like play Tic-Tac-Toe again?")
            game = play_game()
            if not game:
                print("Thanks for playing Tic-Tac-Toe!")
            break
else:
    print("See ya next time!")