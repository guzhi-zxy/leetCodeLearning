# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: merge.py
@time: 2020-04-16 23:15:43
@projectExplain: 56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = Solution().merge(intervals)
    print(res)
