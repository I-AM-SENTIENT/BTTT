def create_board():
    #make a board for the new game
    board = [[0,1,2],
             [3,4,5],
             [6,7,8]]
    return board

def render(board):
    for x in board:
        print(x)
    

def make_move(cords,side,board):
    x = cords[0]
    y = cords[1]
    board[x][y] = side
    return board




def game_check(board):
    #Check if the game is over
    pass

def get_move():
    print("Select the square you want to make a move")
    square=input()
    square = int(square)
    if square >=0 and square<=2:
        x=0
        y=square
    elif square >= 3 and square<=5:
        x=1
        y=square-3
    elif square >= 6 and square<=8: 
        x=2
        y=square-6
    return x,y
    #print(f"Cords are X: {x}, Y: {y}")
