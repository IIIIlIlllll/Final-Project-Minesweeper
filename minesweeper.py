import random
from typing import List, Tuple

def init_board(rows: int, cols: int, num_mines: int) -> Tuple[List[List[str]], List[List[int]]]:
    visible_board = []
    real_board = []
    for x in range(0,rows):
        visible_board.append([])
        for y in range(0,cols):
            visible_board[x].append('□')
    print_board(visible_board)
    input=get_user_action(visible_board)
    while input[0]!='r':
        print("Please reveal a cell first.")
        input=get_user_action(visible_board)
    real_board = place_mines(rows,cols,num_mines,input[1],input[2])
    reveal_cell(input[1],input[2],visible_board,real_board)
    print_board(visible_board)
    return visible_board,real_board
    ###初始化棋盘，生成可见地图和真实地图（含雷及数字)###

def place_mines(rows: int, cols: int, num_mines: int, input_row: int, input_col: int) -> List[List[int]]:
    """
    随机放置地雷并计算每个格子的数字（周围地雷数）。

    返回:
        real_board: 包含地雷('M')和数字(0~8)的地图
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




def print_board(visible_board: List[List[str]]) -> None:
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
    """
    打印当前用户可见的棋盘。

    参数:
        visible_board: 用户视角棋盘
    """



def reveal_cell(row: int, col: int, visible_board: List[List[str]], real_board: List[List[int]]) -> bool:
    """
    打开一个格子，如果是0则展开周围，更新visible_board。

    参数:
        row, col: 要打开的格子位置
        visible_board: 用户可见地图
        real_board: 真实地图

    返回:
        是否踩雷，True 表示踩到地雷，游戏失败
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


def flag_cell(row: int, col: int, visible_board: List[List[str]]) -> None:
    """
    标记或取消标记一个格子为旗帜。

    参数:
        row, col: 要操作的格子位置
        visible_board: 用户可见地图
    """
    if visible_board[row][col]=='F':
        visible_board[row][col]='□'
    else:
        visible_board[row][col]='F'



def check_victory(visible_board: List[List[str]], real_board: List[List[int]]) -> bool:
    """
    检查是否胜利：所有非地雷格子都已打开。

    返回:
        True 表示胜利
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

def get_user_action(visible_board: List[List[str]]) -> Tuple[str, int, int]:
    """
    从用户处获取输入操作，并且确保用户输入合法。

    返回:
        action_type: 'open' 或 'flag'
        row, col: 操作的目标坐标(已经减过1)
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
        if not(action_type == 'r' or action_type == 'f'):
            print("Invalid input. Please enter again. The action must br 'r' or 'f'")
            continue
        if not(1 <= int(row) <= len(visible_board) and 1 <= int(col) <= len(visible_board[0])):
            print(f'Input is outside the board. Please enter again. (row:1-{len(visible_board)}, col:1-{len(visible_board[0])})')
            continue
        if (action_type == 'r' or action_type == 'f') and type(visible_board[int(row)-1][int(col)-1]) == int:
            print('This cell has already been revealed. Please enter again')
            continue
        if action_type == 'r' and visible_board[int(row)-1][int(col)-1] == 'F':
            print('There is a flag in this cell. Please Remove the flag before you reveal this cell. Please enter again')
            continue
        return (action_type, int(row) - 1, int(col) - 1)



def play_game() -> None:
    """
    主游戏循环，控制整个游戏流程。
    """
    """
    设置游戏棋盘的尺寸和雷数，并对用户输入进行验证。
    """
    print('Please enter the number of rows and columns of the game board (5-20), separated by a space')
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
    visible_board,real_board=init_board(num_rows,num_cols,num_mines)
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









