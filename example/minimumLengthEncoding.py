# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: minimumLengthEncoding.py
@time: 2020-03-28 22:40:59
@projectExplain: 820. 单词的压缩编码
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
"""

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        set_words = set(words)
        for word in words:
            word_length = len(word)
            for i in range(1, word_length):
                set_words.discard(word[i:])
        return sum(len(_) + 1 for _ in set_words)


if __name__ == '__main__':
    words = ["time", "me", "bell", 'l']
    res = Solution().minimumLengthEncoding(words)
    print(res)
