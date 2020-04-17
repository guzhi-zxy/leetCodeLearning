# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: canJump.py
@time: 2020-04-17 23:16:16
@projectExplain: 55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length, rightmost = len(nums), 0
        for i in range(length):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= length - 1:
                    return True
        return False

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_index = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= cur_index:
                cur_index = i
            i -= 1
        return cur_index == 0


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 0, 8]
    res = Solution().canJump2(nums)
    print(res)
