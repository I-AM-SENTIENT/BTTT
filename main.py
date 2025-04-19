from board import *
from engine import *
#This should track the move, even for O, odds for X
move = 1

board = create_board()

while(game_check(board) == False):
    render(board)
    if side_to_move(move) == "X":
        board = make_move(get_move(),"X",board)
    elif side_to_move(move) == "O":
        board = make_move(return_ai_move(board),"O",board)
