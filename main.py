from board import *
side_to_move = "X"
board = create_board()
render(board)

board = make_move(get_move(),side_to_move,board)
render(board)