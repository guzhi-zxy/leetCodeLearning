# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: rotate.py
@time: 2020-04-07 22:52:35
@projectExplain: 面试题 01.07. 旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        matrix[:] = matrix[::-1]
        # 然后沿对角线翻转
        for i in range(1, length):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = Solution().rotate(matrix)
    print(res)
