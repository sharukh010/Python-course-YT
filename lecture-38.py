"""
Tic Tac Toe: 
1. We should be able  to store game state 
2. alternatively change user turn 
3. we need to be able to find who is the winner of the game 
      0   1   2
    +---+---+---+
  0 | X | O | X | 
    +---+---+---+
  1 | O | X | O | 
    +---+---+---+
  2 | X |   |   | 
    +---+---+---+

made by: DecodewithSK

"""

# row1 = ["X","O","X"]
# row2 = ["O","X","O"]
# row3 = ["X"," "," "]
# board = [row1,row2,row3] # 2d list 
# print(board[1][1])
def is_valid(row,col):
    if row>=3 or col >=3: 
        return False 
    elif row<0 or col <0:
        return False 
    else:
        return True 
    
def is_occupied(board,row,col):
    if board[row][col] == " ":
        return False 
    else: 
        return True 
def is_winner(board,marker):
    # check in all rows 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == marker:
            return True 

    # check in all the columns 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == marker:
            return True 

    # check in the diagonals 
    if board[0][0] == board[1][1] == board[2][2] == marker:
        return True 
    if board[0][2] == board[1][1] == board[2][0] == marker:
        return True 

    return False 
    
board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

turn = True # marker X
marker = "X"
counter = 0 
while True: 
    board_state = f"""Board: 
    +---+---+---+
    | {board[0][0]} | {board[0][1]} | {board[0][2]} | 
    +---+---+---+
    | {board[1][0]} | {board[1][1]} | {board[1][2]} | 
    +---+---+---+
    | {board[2][0]} | {board[2][1]} | {board[2][2]} | 
    +---+---+---+
    """
    print(board_state)
    if is_winner(board,marker):
        print(f"{marker} is Winner")
        break 
    elif counter == 9:
        print("It's a Tie.")
        break 

    if turn: 
        marker = "X"
    else: 
        marker = "O"
    print(f"{marker}'s Turn: ")
    row = int(input("Enter row number: "))
    col = int(input("Enter col number: "))
    if is_valid(row-1,col-1):
        if is_occupied(board,row-1,col-1):
            print("This cell is already occupied.")
        else:
            board[row-1][col-1] = marker 
            turn = not turn 
            counter += 1 
    else:
        print("Invalid Row/Col number")