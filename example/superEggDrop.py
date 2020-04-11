# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: superEggDrop.py
@time: 2020-04-11 20:00:47
@projectExplain: 887. 鸡蛋掉落
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
"""


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def task(K, T):
            if K == 1:  # 只有1个鸡蛋，可以扔的轮数等于楼层数
                return T
            elif T == 1:  # 只有1层，则不管有多少鸡蛋也只能扔1轮
                return 1
            elif (K, T) in table:
                return table[(K, T)]

            bcaze = task(K - 1, T - 1)  # 鸡蛋怎么扔都碎的情况
            notbcase = task(K, T - 1)  # 鸡蛋怎么扔都不碎的情况
            res = 1 + bcaze + notbcase  # 总轮数
            table[(K, T)] = res
            return res

        table = {}
        T = 1  # 先在第一层毫无顾忌地扔
        while task(K, T) < N:
            T += 1
        return T


if __name__ == '__main__':
    K = 3
    N = 14
    res = Solution().superEggDrop(K, N)
    print(res)
