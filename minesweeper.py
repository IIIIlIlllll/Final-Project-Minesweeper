import random

def init_board(rows: int, cols: int, num_mines: int):
    """
    input:
        rows(int): The number of rows of the board
        cols(int): The number of cols of the board
        num_mines(int): The number of mines

    output:
        visible_board(list[list[int,str]])
        real_board(list[list[int,str]])

    function:
        Initialize the chessboard according to the size input by the user.
    """

    
#Creat visible_board
    visible_board = []
    real_board = []
    for x in range(0,rows):
        visible_board.append([])
        for y in range(0,cols):
            visible_board[x].append('□')
    print_board(visible_board)

#The first time the input is read, to prevent the user from losing at the first step.
    input=get_user_action(visible_board)
    while input[0]!='r':
        print("Please reveal a cell first.")
        input=get_user_action(visible_board)
    real_board = place_mines(rows,cols,num_mines,input[1],input[2])
    reveal_cell(input[1],input[2],visible_board,real_board)
    print_board(visible_board)

    return visible_board,real_board




def place_mines(rows: int, cols: int, num_mines: int, input_row: int, input_col: int) :
    """
    input:
        rows(int): The number of rows of the board
        cols(int): The number of cols of the board
        num_mines(int): The number of mines
        input_row(int): The row entered for the first time
        input_col(int): The col entered for the first time

    output:
        real_board(list[list[int, str]])

    function:
        Create a board with mines randomly. Prevent the user from losing at the first step.
    """


    real_board=[]
    for row in range(rows):
        real_board+=[[0]*cols]
    seed=random.sample(range(rows*cols-1),num_mines)
    seed=[cell for cell in seed if cell<input_row*cols+input_col]+[cell+1 for cell in seed if cell>=input_row*cols+input_col]
    for mine in range(num_mines):
        row=int(seed[mine]/cols)
        col=seed[mine]%cols
        real_board[row][col]='M'
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if 0<=i<rows and 0<=j<cols and type(real_board[i][j])==int:
                    real_board[i][j]+=1
    return real_board




def print_board(visible_board: list[list[int, str]]):
    """
    input:
        visible_board(list[list[int, str]]): Any board

    output:
        None

    function:
        Print the board in the following format:
 0   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
 
 1   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □ 
 2   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □ 
 3   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □ 
 4   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
 5   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
 6   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
 7   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
 8   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
 9   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
10   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
11   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
12   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
13   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
14   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
15   □  □  □  □  □  □  □  □  □  □  □  □  □  □  □

    """


    output=" 0  "
    for col in range(1,len(visible_board[0])+1):
        if col<=9:
            output+=' '+str(col)+' '
        else:
            output+=' '+str(col)
    print(output)
    print(' ')
    for row in range(len(visible_board)):
        if row<9:
            output=' '+str(row+1)+'  '
        else:
            output=str(row+1)+'  '
        for col in range(len(visible_board[0])):
            output+=' '+str(visible_board[row][col])+' '
        print(output)
    return None




def reveal_cell(row: int, col: int, visible_board: list[list[int, str]], real_board: list[list[int, str]]):
    """
    input:
        row(int): The input row 
        col(int): The input col 
        visible_board(list[list[int, str]]): Current situation of the board
        real_board(list[list[int, str]]): The real board

    output:
        bool: Whether stepped on a mine

    function:
        Reveal a cell, if the cell is 0, reveal the 8 cells around it. (Will run recursively)
    """


    if real_board[row][col]=='M':
        visible_board[row][col]=='M'
        return True
    if visible_board[row][col]!=real_board[row][col]:
        visible_board[row][col]=real_board[row][col]
        if visible_board[row][col]==0:
            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if 0<=i<len(real_board) and 0<=j<len(real_board[0]) and (not (i==row and j==col)):
                        reveal_cell(i,j,visible_board,real_board)
    return False




def flag_cell(row: int, col: int, visible_board: list[list[int, str]]) -> None:
    """
    input:
        row(int): The input row 
        col(int): The input col 
        visible_board(list[list[int, str]]): Current situation of the board

    output:
        None

    function:
        Place a flag on a cell without flag, or remove the flag on a cell that already has a flag.
    """


    if visible_board[row][col]=='F':
        visible_board[row][col]='□'
    else:
        visible_board[row][col]='F'




def check_victory(visible_board: list[list[int, str]], real_board: list[list[int, str]]):
    """
    input:
        visible_board(list[list[int, str]]): Current situation of the board
        real_board(list[list[int, str]]): The real board

    output:
        bool: Whether win the game

    function:
        Compare the visible_board and the real_board. If every cells without mines are revealed or there is flag on every cells with mines.

    """


    output=True
    for row in range(len(visible_board)):
        for col in range(len(visible_board[row])):
            if type(real_board[row][col])==int and type(visible_board[row][col])!=int:
                output=False
                break
        if output==False:
            break
    if output==True:
        return True
    output=True
    for row in range(len(visible_board)):
        for col in range(len(visible_board[row])):
            if real_board[row][col]=='M' and visible_board[row][col]!='F':
                output=False
                break
        if output==False:
            break
    return output

def get_user_action(visible_board: list[list[int, str]]):
    """
    input:
        visible_board(list[list[int, str]]): Current situation of 

    output:
        action_type(str): Action user want to do, 'r' to reveal a cell or 'f' to place or remove a flag on a cell
        row: The row of the cell to be dealt with. (Subtract one and make it compatible with Python)
        col: The col of the cell to be dealt with. (Subtract one and make it compatible with Python)

    function:
        Obtain the input operation from the user and ensure that the user input is valid.
    """


    print("Please enter 'r' to reveal a cell or 'f' to place or remove a flag on a cell. Then enter The coordinates of the cell, separated by a space.(eg. r 1 1)")
    while True:
        try:
            action_type, row, col = input().split()
            row = int(row)
            col = int(col)
        except ValueError:
            print('Invalid input. Please enter again.(eg. r 1 1)')
            continue

        #Make sure action type is correct
        if not(action_type == 'r' or action_type == 'f'):
            print("Invalid input. Please enter again. The action must br 'r' or 'f'")
            continue

        #Make sure the position is in the board
        if not(1 <= int(row) <= len(visible_board) and 1 <= int(col) <= len(visible_board[0])):
            print(f'Input is outside the board. Please enter again. (row:1-{len(visible_board)}, col:1-{len(visible_board[0])})')
            continue

        #Make sure that the user don't do action on the cell that have already been revealed
        if (action_type == 'r' or action_type == 'f') and type(visible_board[int(row)-1][int(col)-1]) == int:
            print('This cell has already been revealed. Please enter again')
            continue

        #Make sure that the user don't reveal a cell with flag on it.
        if action_type == 'r' and visible_board[int(row)-1][int(col)-1] == 'F':
            print('There is a flag in this cell. Please Remove the flag before you reveal this cell. Please enter again')
            continue

        return (action_type, int(row) - 1, int(col) - 1)




def play_game():
    """
    The main game loop controls the entire game process.
    """


    print("Game start! Instruction: The mine is represented by 'M', the flag is represented by 'F', '□' means the cell hasn't been revealed. The number of the cell means how many mines are there in the 8 cells around the cell.")
    print('Please enter the number of rows and columns of the game board (5-20), separated by a space')

    #Set up the size of board and the number of mines
    while True:
        try:
            num_rows, num_cols = input().split()
            num_rows = int(num_rows)
            num_cols = int(num_cols)
        except ValueError:
            print('Invalid format. Please enter two numbers separated by a space.')
            continue
        if not(5 <= num_rows <= 20 and 5 <= num_cols <= 20):
            print('Invalid range. Both numbers must be between 5 and 20. Please enter again.')
            continue
        break
    print(f'Please enter the number of mines (1-{num_rows*num_cols-2})')
    max_mines = num_rows * num_cols - 2
    while True:
        try:
            num_mines = input()
            num_mines = int(num_mines)
        except ValueError:
            print('Invalid format. Please enter a single number.')
            continue
        if not(1 <= num_mines <= max_mines):
            print(f'Invalid range. The number of mines must be between 1 and {max_mines}. Please enter again.')
            continue
        break

    #Initialize
    visible_board,real_board=init_board(num_rows,num_cols,num_mines)

    #Main game loop
    while True:
        action=get_user_action(visible_board)
        if action[0]=='r':
            if reveal_cell(action[1],action[2],visible_board,real_board)==True:
                print_board(real_board)
                print('You lose!')
                break
            if  check_victory(visible_board,real_board):
                print_board(real_board)
                print('Congratulations! You win!')
                break
            else:
                print_board(visible_board)
        if action[0]=='f':
            flag_cell(action[1],action[2],visible_board)
            if  check_victory(visible_board,real_board):
                print_board(real_board)
                print('Congratulations! You win!')
                break
            else:
                print_board(visible_board)


if __name__ == "__main__":
    play_game()









