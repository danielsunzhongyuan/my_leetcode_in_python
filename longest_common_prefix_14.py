class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ret = ""
        min_length = len(strs[0])
        min_str = strs[0]
        for s in strs:
            if min_length > len(s):
                min_length = len(s)
                min_str = s
        stop = False
        for i in range(min_length):
            if stop:
                break
            for s in strs:
                if s[i] != min_str[i]:
                    stop = True
                    break
            else:
                ret += min_str[i]
        return ret
