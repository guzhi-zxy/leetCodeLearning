# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: numRookCaptures.py
@time: 2020-03-26 23:25:35
@projectExplain: 999. 车的可用捕获量
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
返回车能够在一次移动中捕获到的卒的数量。
"""
from typing import List

import numpy as np


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        if not board: return 0
        R = [(x, y) for x in range(len(board)) for y in range(len(board)) if board[x][y] == 'R'][0]
        R_x = ''.join(board[R[0]]).replace('.', '')
        R_y = ''.join(board[i][R[1]] for i in range(len(board))).replace('.', '')
        return sum((R_x.count("pR"), R_x.count("Rp"), R_y.count("pR"), R_y.count("Rp")))

    def numRookCaptures2(self, board: List[List[str]]) -> int:
        # 用numpy array 获取列 ... array[:, n]
        if not board: return 0
        board_array = np.array(board)
        R = [(x, y) for x in range(len(board)) for y in range(len(board)) if board[x][y] == 'R'][0]
        R_x = ''.join(board[R[0]]).replace('.', '')
        R_y = ''.join(board_array[:, R[1]]).replace('.', '')
        return sum((R_x.count("pR"), R_x.count("Rp"), R_y.count("pR"), R_y.count("Rp")))


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]]
    res = Solution().numRookCaptures(board)
    print(res)
