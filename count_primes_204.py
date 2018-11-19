# @author: Zhongyuan Sun
# @question: 204. count-primes
# @time: O(n) space: O(n)
# @runtime: 1632 ms, beats 29%
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        a = [True] * n
        a[0] = a[1] = False
        for i in range(4, n, 2):
            a[i] = False
        for i in range(3, n, 2):
            if a[i]:
                tmp = i * 2
                while tmp < n:
                    a[tmp] = False
                    tmp += i
        return sum(a)
        # return a.count(True)
