import random

def display_board(board):
    print('\n' * 10)
    print (board[1]+'|'+board[2]+'|'+board[3])
    print ('-----')
    print (board[4]+'|'+board[5]+'|'+board[6])
    print ('-----')
    print (board[7]+'|'+board[8]+'|'+board[9])


test_board = [' '] * 10
display_board(test_board)


def player_input():
    marker = ' '

    while marker not in ['x', 'o']:
        marker = input('Please enter your marker (X or O): ').lower().strip()
        if marker not in ['x', 'o']:
            print("Sorry, please enter X or O")
    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        #
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        #
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark) or
        #
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark)
                                                                        )


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    while True:
        position = int(input('Please enter your position (1-9): '))
        if position not in range(1, 10):
            print("Invalid number. Choose 1-9.")
            continue
        if not space_check(board, position):
                print("This position is already taken. Choose another one.")
                continue
        return position


def replay():
    while True:
        choice = input('Do you want to play again? (Yes/No): ').lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

print("Welcome to Tic Tac Toe!")

while True:
    test_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " goes first")
    game_on = True

    while game_on:

        if turn == "Player 1":
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)

            if win_check(test_board, player1_marker):
                display_board(test_board)
                print("Player 1 wins!")
                game_on = False
            else:
                if full_board_check(test_board):
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)

            if win_check(test_board, player2_marker):
                display_board(test_board)
                print("Player 2 wins!")
                game_on = False
            else:
                if full_board_check(test_board):
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        break
