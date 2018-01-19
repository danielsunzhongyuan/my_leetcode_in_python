class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            return self.reversePositiveNumber(x)
        elif x < 0:
            return 0 - self.reversePositiveNumber(-x)
        else:
            return 0

    def reversePositiveNumber(self, x):
        if x <= 0:
            return 0
        while x%10 == 0:
            x /= 10
        xStr = str(x)
        y = int(xStr[::-1])
        if y > (2<<30):
            return 0
        return y

