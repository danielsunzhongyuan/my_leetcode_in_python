class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution One
        # res = 0
        # length = len(s)
        # i = 0
        # while i < length:
        #     if s[i] != " ":
        #         break
        #     i += 1
        # while i < length:
        #     while i < length and s[i] != " ":
        #         i += 1
        #     res += 1
        #     while i < length and s[i] == " ":
        #         i += 1
        # return res
        
        # Solution Two
        # s = s.strip()
        # if not s:
        #     return 0
        # res = 0
        # length = len(s)
        # for i in range(1, length):
        #     if " " == s[i] and s[i-1] != " ":
        #         res += 1
        # return res + 1
        
        # Solution Three
        s = " " + s
        res = 0
        for i, x in enumerate(s):
            if x != " " and s[i-1] == " ":
                res += 1
        return res
