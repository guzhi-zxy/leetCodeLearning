# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: trap.py
@time: 2020-04-04 22:21:23
@projectExplain: 42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3: return 0
        cnt, index = 0, 0
        stack = []
        while index < length:
            while len(stack) and height[index] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack): break
                h = min(height[stack[-1]], height[index]) - height[top]
                dist = index - stack[-1] - 1
                cnt += h * dist
            stack.append(index)
            index += 1
        return cnt


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = Solution().trap(height)
    print(res)
