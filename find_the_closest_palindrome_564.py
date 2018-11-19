"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        n_int = int(n)
        if n_int < 11:
            return str(n_int - 1)
        if n_int == 11:
            return "9"
        if n_int < 17:
            return "11"

        length = len(n)
        possibles = []
        if length % 2 == 0:
            left_half = int(n[:length / 2])
            possibles.append(left_half * (10 ** (length / 2)) + int(str(left_half)[::-1]))

            left_minus_one = left_half - 1
            if len(str(left_minus_one)) == length / 2:
                possibles.append(left_minus_one * (10 ** (length / 2)) + int(str(left_minus_one)[::-1]))
            else:
                possibles.append(10 ** (length - 1) - 1)

            left_plus_one = left_half + 1
            if len(str(left_plus_one)) == length / 2:
                possibles.append(left_plus_one * (10 ** (length / 2)) + int(str(left_plus_one)[::-1]))
            else:
                possibles.append(10 ** (length) + 1)
        else:
            left_half = int(n[:length / 2 + 1])
            possibles.append(left_half * (10 ** (length / 2)) + int(n[:length / 2][::-1]))

            left_minus_one = left_half - 1
            if len(str(left_minus_one)) == (length / 2 + 1):
                possibles.append(left_minus_one * (10 ** (length / 2)) + int(str(left_minus_one)[:-1][::-1]))
            else:
                possibles.append(left_minus_one * (10 ** (length / 2)) + int(str(left_minus_one)[::-1]))
            left_plus_one = left_half + 1
            if len(str(left_plus_one)) == (length / 2 + 1):
                possibles.append(left_plus_one * (10 ** (length / 2)) + int(str(left_plus_one)[:-1][::-1]))
            else:
                possibles.append(left_plus_one / 10 * (10 ** (length / 2 + 1)) + int(str(left_plus_one / 10)[::-1]))
        possibles.sort()

        diff, ret = possibles[-1], 0
        for p in possibles:
            if abs(n_int - p) > 0 and abs(n_int - p) < diff:
                ret = p
                diff = abs(n_int - p)
        return str(ret)


if __name__ == "__main__":
    a = Solution()
    print a.nearestPalindromic("1000")
    print a.nearestPalindromic("11")
    print a.nearestPalindromic("9999")
    print a.nearestPalindromic("99")
    print a.nearestPalindromic("999")
    print a.nearestPalindromic("1001")
    print a.nearestPalindromic("101")
    print a.nearestPalindromic("1111")
