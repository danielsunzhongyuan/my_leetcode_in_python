class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        res = 0
        if s == "":
            return res
        mapping = dict(zip(string.ascii_uppercase, [i for i in range(1, 27)]))
        for c in s:
            res = res*26 + mapping[c]
        return res
