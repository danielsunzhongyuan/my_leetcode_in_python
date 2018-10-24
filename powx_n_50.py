class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Solution One: 28ms
        # result = x
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 1 / self.myPow(x, -n)
        # elif n % 2 == 1:
        #     return x * self.myPow(x * x, n / 2)
        # else:
        #     return self.myPow(x * x, n / 2)
        
        # Solution Two: 20ms
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2 == 0:
            result = self.myPow(x, n/2)
            return result*result
        else:
            result = self.myPow(x, n/2)
            return x*result*result

