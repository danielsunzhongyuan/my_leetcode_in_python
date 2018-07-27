class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        res = ""
        if n <= 0:
            return res
        mapping = dict(zip([i for i in range(26)], string.ascii_uppercase))
        while n:
            res += mapping[(n-1)%26]
            n = (n-1)/26
        return res[::-1]
