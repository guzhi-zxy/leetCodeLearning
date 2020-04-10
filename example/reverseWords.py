# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: reverseWords.py
@time: 2020-04-10 20:55:51
@projectExplain: 151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.split()[::-1])
        # return ' '.join(reversed(s.split()))
        lst = []
        res = s
        a = ''
        k = 0
        for r in res:
            if r == ' ':
                k += 1
                if k <= 1:
                    lst.append(a)
                    a = ''
                else:
                    k -= 0
            else:
                a += r
                k = 0
        if a:
            lst.append(a)
        return ' '.join(reversed(lst))


if __name__ == '__main__':
    # s = "  hello world!  "
    # s = "the sky is blue"
    s = "a good   example"
    res = Solution().reverseWords(s)
    print(res)
