class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # Solution 1: works
        n = int(n)
        for k in xrange(int(math.log(n, 2)), 1, -1):
            a = int(n ** k ** -1)
            if (1 - a**(k+1)) // (1-a) == n:
                return str(a)
        return str(n-1)

        # Solution 2: TLE
        # length = len(n)
        # if n[-1] in ("1", "3", "5", "7", "9"):
        #     for i in xrange(2, long(n)):
        #         tmp = 1 + i
        #         while len(str(tmp)) <= length and str(tmp) != n:
        #             tmp = tmp * i + 1
        #         if str(tmp) == n:
        #             return str(i)
        # # if n is an even number, the k would definitely be an odd number
        # else:
        #     for i in xrange(3, long(n), 2):
        #         tmp = 1 + i
        #         while len(str(tmp)) <= length and str(tmp) != n:
        #             tmp = tmp * i + 1
        #         if str(tmp) == n:
        #             return str(i)
