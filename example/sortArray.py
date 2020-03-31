# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: sortArray.py
@time: 2020-03-31 12:25:43
@projectExplain: 912. 排序数组
给你一个整数数组 nums，将该数组升序排列。
"""
from typing import List


class Solution:
    # 计数排序
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums_length = len(nums)
        nums_min = min(nums)
        nums_max = max(nums)
        tmp = [0] * (nums_max - nums_min + 1)
        for num in nums:
            tmp[num - nums_min] += 1
        j = 0
        for i in range(nums_length):
            while tmp[j] == 0:
                j += 1
            nums[i] = j + nums_min
            tmp[j] -= 1
        return nums

    def sortArray2(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums_length = len(nums)
        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 0]
    res = Solution().sortArray(nums)
    print(res)
