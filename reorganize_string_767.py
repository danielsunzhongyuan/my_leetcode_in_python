"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = sorted(sorted(S), key=S.count)
        h = len(a) / 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])
