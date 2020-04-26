# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: moveZeroes.py
@time: 2020-04-23 23:25:03
@projectExplain: 283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    res = Solution().moveZeroes(nums)
    print(res)
