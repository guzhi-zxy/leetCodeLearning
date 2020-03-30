# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: lastRemaining.py
@time: 2020-03-30 23:22:18
@projectExplain: 面试题62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
"""

'''
约瑟夫环经典问题。
f(n)代表第n个人中，存活到最后的人的最终下标f(n)代表第n个人中，存活到最后的人的最终下标
最终剩下一个人时的安全位置肯定为0，反推安全位置在人数为n时的编号
人数为1： f(1) = 0
人数为2： f(2) = (0 + m) % 2
人数为3： f(3) = ((0+m) % 2 + m) % 3
人数为4： f(4) = (((0+m) % 2 + m) % 3 + m) % 4
...
人数为n: f(n) = (f(n-1) + m) % nf(n)=(f(n−1)+m)
'''


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return (self.lastRemaining(n - 1, m) + m) % n if n else 0


if __name__ == '__main__':
    n = 5
    m = 3
    res = Solution().lastRemaining(n, m)
    print(res)
