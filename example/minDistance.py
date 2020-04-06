# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: minDistance.py
@time: 2020-04-06 20:30:24
@projectExplain: 72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # 第一列
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        # 第一行
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)
