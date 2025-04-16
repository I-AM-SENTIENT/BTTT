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
    #Horizontal checks
    if board[0][0] == board[0][1] == board[0][2] and not None:
        #Win
        pass
    elif board[1][0] == board[1][1] == board[1][2] and not None:
        #Win
        pass
    elif board[2][0] == board[2][1] == board[2][2] and not None:
        #Win
        pass
    #Vertical checks
    elif board[0][0] == board[1][0] == board[2][0] and not None:
        #Win
        pass
    elif board[0][1] == board[1][1] == board[2][1] and not None:
        #Win
        pass
    elif board[0][2] == board[1][2] == board[2][2] and not None:
        #Win
        pass
    #Diagonal checks
    elif board[0][0] == board[1][1] == board[2][2] and not None:
        #Win
        pass
    elif board[2][0] == board[1][1] == board[0][2] and not None:
        #Win
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
