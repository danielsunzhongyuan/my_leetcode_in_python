"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Solution One
        # ans=n
        # while ans>m:
        #     ans=ans&(ans-1)
        # return ans

        # Solution Two
        count = 0
        while m < n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count
