# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hasGroupsSizeX.py
@time: 2020-03-27 21:30:25
@projectExplain: 914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
"""
from typing import List
from math import gcd
from collections import Counter
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck: return False
        print(reduce(gcd, list(Counter(deck).values())) )
        return True if reduce(gcd, list(Counter(deck).values())) >= 2 else False


if __name__ == '__main__':
    deck = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    res = Solution().hasGroupsSizeX(deck)
    print(res)
