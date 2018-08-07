"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a != 0 and b != 0:
            a, b = a^b, (a&b)<<1
            if a > 1<<31 or b > 1<<31:
                a %= 1<<31
                b %= 1<<31
        return a or b

if __name__ == "__main__":
	a = Solution()
	print a.getSum(-14, 16)
