
# игральная даска
def display_board(board):
    print('\n' * 100)
    print (board[1]+'|'+board[2]+'|'+board[3])
    print ('-----------')
    print (board[4]+'|'+board[5]+'|'+board[6])
    print ('-----------')
    print (board[7]+'|'+board[8]+'|'+board[9])
test_board = ['   '] * 10
display_board(test_board)

#выбор игрока
def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Please enter your marker( X or O ): ')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
player_input()

#
def place_marker(board, marker, position):
    board[position] = marker
    #мне это надо оставлять? я протестил работает
    place_marker(test_board, ' @ ', 8)
    display_board(test_board)

#выиграшные комбинации
def win_check(board, mark):
    return (
        #горизонтально
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        #диагональ
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark) or
        #вертикально
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark)
                                                                        )
print(win_check(test_board,'X'))

#
def choose_first():
    #у меня почему то не импортируется в пейчарме рандом
    import random




