# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: generateParenthesis.py
@time: 2020-04-09 23:00:51
@projectExplain: 22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def task(s, l, r):
            if len(s) == 2 * n:
                res.append(''.join(s))
                return

            if l < n:
                s.append('(')
                task(s, l + 1, r)
                s.pop()
            if r < l:
                s.append(')')
                task(s, l, r + 1)
                s.pop()

        task([], 0, 0)

        return res


if __name__ == '__main__':
    n = 3
    res = Solution().generateParenthesis(n)
    print(res)
