# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: gameOfLife.py
@time: 2020-04-02 21:53:03
@projectExplain: 289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
"""
from typing import List
import numpy as np


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        # 下面两行做zero padding
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1:1 + r, 1:1 + c] = np.array(board)
        print(board_exp)
        # 设置卷积核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围8个位置的状态
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                # 按照题目规则进行判断
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1

    def gameOfLife2(self):
        '''
        常规思路：
        对于每个坐标位置，都统计其周边活细胞个数（记为cnt），并以此作为其下轮生死依据：
        生存定律给了4条，实际上只有以下3种情形：
        当cnt=2时，保持上轮状态不变：即之前活则下轮活、之前死则下轮死
        当cnt=3时，下轮无条件的活，无论之前生死
        其余情况，即cnt<2或cnt>3，下轮无条件的死，无论之前生死
        为了确保不会在更新前一个细胞状态时影响后续判断（即题目要求的同步更新），这里考虑用列表推导式实现同时赋值(实际上相当于占用了内存作为临时空间)
        当然，如果用一个copy.deepcopy(board)副本其效果是一样的，只不过没有列表推导来得爽！
        注：对于嵌套列表，在inplace更新赋值时要加冒号，即用board[:]=……而不能用board=……
        '''
        if not board or not board[0]:
            return

        def isValid(x, y):  # 判断给定坐标是否在区间内
            return 0 <= x < m and 0 <= y < n

        m, n = len(board), len(board[0])
        delt = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def isAlive(i, j):  # 根据给定坐标判断其下轮生死
            cnt = sum([board[i + di][j + dj] for di, dj in delt if isValid(i + di, j + dj)])
            return board[i][j] if cnt == 2 else (1 if cnt == 3 else 0)

        board[:] = [[isAlive(i, j) for j in range(n)] for i in range(m)]


if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    res = Solution().gameOfLife(board)
    print(res)
