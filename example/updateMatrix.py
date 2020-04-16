# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: updateMatrix.py
@time: 2020-04-15 23:12:41
@projectExplain: 542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。
"""
from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            x, y = q.popleft()
            for ni, nj in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[x][y] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist


if __name__ == '__main__':
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]
              ]
    res = Solution().updateMatrix(matrix)
    print(res)
