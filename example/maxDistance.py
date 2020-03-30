# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: maxDistance.py
@time: 2020-03-29 11:09:02
@projectExplain: 1162. 地图分析
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。
"""

from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        grid_length, n = len(grid), len(grid[0])
        steps = -1
        stack = [(i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == 1]
        if len(stack) == 0 or len(stack) == grid_length * n: return steps
        while len(stack) > 0:
            for _ in range(len(stack)):
                x, y = stack.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= xi < grid_length and 0 <= yj < grid_length and grid[xi][yj] == 0:
                        stack.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    res = Solution().maxDistance(grid)
    print(res)
