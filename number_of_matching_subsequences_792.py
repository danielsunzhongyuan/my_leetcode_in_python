#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/20 21:25
# @Author   : Zhongyuan Sun

"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].


Solution:
1. 给words统计去重很关键，可以少判断很多次
2. 用python自带的 find，比自己写 binarySearch 要好很多
"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        cnt_words = {}
        for word in words:
            cnt_words[word] = cnt_words.get(word, 0) + 1
        # Solution Three: 224ms
        for word in cnt_words.keys():
            if self.isSubsequence(word, S):
                count += cnt_words[word]
        return count

        # Solution Two: not good
        # def binarySearch(idx, l, start, end):
        #     while start <= end:
        #         mid = start + (end-start)/2
        #         if l[mid] < idx:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        #     return -1 if start == len(l) else l[start]
        # mapping = {}
        # for idx, c in enumerate(S):
        #     if c in mapping:
        #         mapping[c].append(idx)
        #     else:
        #         mapping[c] = [idx]
        # for word in cnt_words.keys():
        #     prev = -1
        #     ok = True
        #     for c in word:
        #         if c not in mapping:
        #             ok = False
        #             break
        #         l = mapping[c]
        #         prev = binarySearch(prev, l, 0, len(l)-1)
        #         if prev == -1:
        #             ok = False
        #             break
        #         prev += 1
        #     if ok:
        #         count += cnt_words[word]
        # return count

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution One: slow
        # i, j = 0, 0
        # while i < len(s):
        #     while j < len(t) and s[i] != t[j]:
        #         j += 1
        #     if j >= len(t):
        #         return False
        #     i += 1
        #     j += 1
        # return True

        # Solution Two:
        # def binarySearch(idx, l, start, end):
        #     while start <= end:
        #         mid = start + (end-start)/2
        #         if l[mid] < idx:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        #     return -1 if start == len(l) else l[start]
        # if "" == s:
        #     return True
        # if "" == t:
        #     return False
        # mapping = {}
        # for idx, c in enumerate(t):
        #     if c in mapping:
        #         mapping[c].append(idx)
        #     else:
        #         mapping[c] = [idx]
        # prev = -1
        # for c in s:
        #     if c not in mapping:
        #         return False
        #     l = mapping[c]
        #     prev = binarySearch(prev, l, 0, len(l)-1)
        #     if prev == -1:
        #         return False
        #     prev += 1
        # return True

        # Solution Three:
        idx = 0
        for c in s:
            idx = t.find(c, idx)
            if idx == -1:
                return False
            idx += 1
        return True
