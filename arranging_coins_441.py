class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 == n:
            return 0
        res = int(math.sqrt(2*n))
        if res*(res+1)/2 < n:
            while not res*(res+1)/2 <= n < (res+1)*(res+2)/2:
                res += 1
        elif res*(res+1)/2 > n:
            while not res*(res+1)/2 <= n < (res+1)*(res+2)/2:
                res -= 1
        return res
