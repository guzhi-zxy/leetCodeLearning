# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: movingCount.py
@time: 2020-04-08 23:09:53
@projectExplain: 面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
"""
from collections import deque


class Solution:
    '''
    BFS
    '''

    def movingCount(self, m: int, n: int, k: int) -> int:
        def add_coor(a, b):
            ans = 0
            for _ in (a, b):
                while _ > 0:
                    ans += _ % 10
                    _ //= 10
            return ans

        marked = set()  # 将访问过的点添加到集合marked中,从(0,0)开始
        queue = deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            if (x, y) not in marked and add_coor(x, y) <= k:
                marked.add((x, y))
                for dx, dy in [(1, 0), (0, 1)]:  # 仅考虑向右和向下即可
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        queue.append((x + dx, y + dy))

        return len(marked)


class Solution2:
    '''
    DFS
    '''

    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumofDigit(x, y):
            result = 0
            while x > 0:
                result += x % 10
                x //= 10
            while y > 0:
                result += y % 10
                y //= 10
            return result

        def dfs(i, j):
            if i == m or j == n or sumofDigit(i, j) > k or (i, j) in marked:
                return
            marked.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)

        marked = set()
        dfs(0, 0)
        return len(marked)


if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    res = Solution().movingCount(m, n, k)
    print(res)
