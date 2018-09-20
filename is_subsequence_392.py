#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/20 21:28
# @Author   : Zhongyuan Sun

"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""


class Solution(object):
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

        # Solution Two: better
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

        # Solution Three: Fast
        idx = 0
        for c in s:
            idx = t.find(c, idx)
            if idx == -1:
                return False
            idx += 1
        return True
