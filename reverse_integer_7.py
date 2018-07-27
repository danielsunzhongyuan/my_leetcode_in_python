# -*- encoding=utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


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
        while x % 10 == 0:
            x /= 10
        xStr = str(x)
        y = int(xStr[::-1])
        if y > (2 << 30):
            return 0
        return y
