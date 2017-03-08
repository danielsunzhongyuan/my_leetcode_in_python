class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # s = sorted(s)
        # t = sorted(t)
        # length = len(s)
        # for i in range(length):
        #     if s[i] != t[i]:
        #         return t[i]
        # return t[-1]

        # sumS = sum([ord(x) for x in s])
        # sumT = sum([ord(x) for x in t])
        # return chr(sumT-sumS)

        # return chr(sum([ord(x) for x in t]) - sum([ord(x) for x in s]))

        return chr(reduce(lambda x,y: x^y, map(ord, s+t)))
