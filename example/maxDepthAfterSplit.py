# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: maxDepthAfterSplit.py
@time: 2020-04-01 22:32:35
@projectExplain: 1111. 有效括号的嵌套深度
有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「有效括号字符串」部分。
嵌套深度 depth 定义：即有效括号字符串嵌套的层数，depth(A) 表示有效括号字符串 A 的嵌套深度。详情参见题末「嵌套深度」部分。
给你一个「有效括号字符串」 seq，请你将其分成两个不相交的有效括号字符串，A 和 B，并使这两个字符串的深度最小。
不相交：每个 seq[i] 只能分给 A 和 B 二者中的一个，不能既属于 A 也属于 B 。
A 或 B 中的元素在原字符串中可以不连续。
A.length + B.length = seq.length
max(depth(A), depth(B)) 的可能取值最小。
划分方案用一个长度为 seq.length 的答案数组 answer 表示，编码规则如下：

answer[i] = 0，seq[i] 分给 A 。
answer[i] = 1，seq[i] 分给 B 。
如果存在多个满足要求的答案，只需返回其中任意 一个 即可。
"""

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        seq_length = len(seq)
        res = [0] * seq_length
        for i in range(1, seq_length):
            if seq[i] == seq[i - 1]:
                res[i] = 1 - res[i - 1]
            else:
                res[i] = res[i - 1]

        return res

    def maxDepthAfterSplit2(self, seq: str) -> List[int]:
        return [(i & 1) ^ (s == ')') for i, s in enumerate(seq)]

if __name__ == '__main__':
    seq = "(()())"
    res = Solution().maxDepthAfterSplit(seq)
    print(res)
