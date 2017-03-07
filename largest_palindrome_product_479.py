# TLE when n equals 8

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        import math
        res = 0
        max_n_digits = 10**n - 1
        min_n_digits = 10**(n-1)
        for left in xrange(max_n_digits, min_n_digits, -1):
            x = left * min_n_digits * 10 + int(str(left)[::-1])
            for factor in xrange(max_n_digits, int(math.sqrt(x))-1, -1):
                if x%factor == 0 and (min_n_digits<=x/factor<=max_n_digits):
                    res = x
                    break
            if res:
                break
        return ((left % 1337)*min_n_digits*10 + int(str(left)[::-1])%1337)%1337
