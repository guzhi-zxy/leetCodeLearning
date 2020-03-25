# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: surfaceArea.py
@time: 2020-03-25 22:54:42
@projectExplain: 892. 三维形体的表面积
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。
"""

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cnt += 4 * grid[i][j] + 2
                if i:
                    cnt -= 2 * min(grid[i - 1][j], grid[i][j])
                if j:
                    cnt -= 2 * min(grid[i][j - 1], grid[i][j])

        return cnt


if __name__ == '__main__':
    grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    res = Solution().surfaceArea(grid)
    print(res)
