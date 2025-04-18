from board import *

#This should track the move, even for O, odds for X
move = 1

board = create_board()

while(game_check(board) == False):
    render(board)
    board = make_move(get_move(),side_to_move(move),board)
    move +=1