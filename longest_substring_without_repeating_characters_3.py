class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        # Solution 1
        # res = 1
        # slow_index = 0
        # for i in range(1, length):
        #     if s[i] in s[slow_index:i]:
        #         slow_index += s[slow_index:i+1].index(s[i]) + 1
        #     if res < i - slow_index + 1:
        #         res = i - slow_index + 1
        # return res
        
        # Solution 2
        res = 1
        charactor_index_mapping = {}
        slow_index = 0
        charactor_index_mapping[s[0]] = 0
        for i in range(1, length):
            if charactor_index_mapping.get(s[i], -1) > -1 and charactor_index_mapping.get(s[i]) >= slow_index:
                if res < i - slow_index:
                    res = i - slow_index
                slow_index = charactor_index_mapping.get(s[i]) + 1
            else:
                if res < i - slow_index + 1:
                    res = i - slow_index + 1
            charactor_index_mapping[s[i]] = i
        return res
