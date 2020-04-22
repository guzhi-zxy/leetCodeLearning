# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: intersection_349.py
@time: 2020-04-22 23:13:23
@projectExplain: 349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        哈希表（不使用额外空间）
        '''
        if not nums1 or not nums2:
            return []
        dic = {}
        for i in nums1:
            if not dic.get(i):
                dic[i] = 1
        n = len(nums2)
        i, j = 0, n - 1
        while i < j:
            if dic.get(nums2[i]):
                dic[nums2[i]] -= 1
                i += 1
            else:
                nums2[i], nums2[j] = nums2[j], nums2[i]
                j -= 1
        if dic.get(nums2[i]):
            i += 1
        return nums2[0:i]


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = Solution().intersection2(nums1, nums2)
    print(res)
