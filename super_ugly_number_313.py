class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_numbers = [1]
        length_primes = len(primes)
        pointers = [0]*length_primes
        while len(ugly_numbers) < n:
            uglys = [0] * length_primes
            for i in xrange(length_primes):
                uglys[i] = ugly_numbers[pointers[i]] * primes[i]
            next_ugly = min(uglys)
            ugly_numbers.append(next_ugly)
            for i in xrange(length_primes):
                if next_ugly == uglys[i]:
                    pointers[i] += 1
        return ugly_numbers[n-1]
