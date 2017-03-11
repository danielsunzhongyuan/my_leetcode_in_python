class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        res = 1
        slow_index = 0
        for i in range(1, length):
            if s[i] in s[slow_index:i]:
                slow_index += s[slow_index:i+1].index(s[i]) + 1
            if res < i - slow_index + 1:
                res = i - slow_index + 1
        return res
