import random
from typing import List, Tuple

def init_board(rows: int, cols: int, num_mines: int) -> Tuple[List[List[str]], List[List[int]]]:
    visible_board = []
    real_board = []
    for x in range(0,rows):
        visible_board.append([])
        for y in range(0,cols):
            visible_board[x].append('□')
        real_board = place_mines(rows,cols,num_mines)
    return visible_board,real_board


def place_mines(rows: int, cols: int, num_mines: int) -> List[List[int]]:
    """
    随机放置地雷并计算每个格子的数字（周围地雷数）。

    返回:
        real_board: 包含地雷('M')和数字(0~8)的地图
    """
    output=[]
    for row in rows:
        output+=[0]*cols


def print_board(visible_board: List[List[str]]) -> None:
    print(' '.join(map(str, list(range(0, len(visible_board)+1)))))
    for x in range (0, len(visible_board)):
            print(str(x+1) + ' ' + (' '.join(visible_board[x])))


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
    pass


def flag_cell(row: int, col: int, visible_board: List[List[str]]) -> None:
    """
    标记或取消标记一个格子为旗帜。

    参数:
        row, col: 要操作的格子位置
        visible_board: 用户可见地图
    """
    pass


def check_victory(visible_board: List[List[str]], real_board: List[List[int]]) -> bool:
    """
    检查是否胜利：所有非地雷格子都已打开。

    返回:
        True 表示胜利
    """
    pass


def get_user_action() -> Tuple[str, int, int]:
    """
    从用户处获取输入操作。

    返回:
        action_type: 'open' 或 'flag'
        row, col: 操作的目标坐标
    """
    pass


def play_game() -> None:
    """
    主游戏循环，控制整个游戏流程。
    """
    pass

if __name__ == "__main__":
    play_game()


