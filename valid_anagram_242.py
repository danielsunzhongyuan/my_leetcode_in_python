class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # lengthS = len(s)
        # lengthT = len(t)
        # if lengthS != lengthT:
        #     return False
        return sorted(s) == sorted(t)