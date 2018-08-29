"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

"""

class SolutionLTE(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        numbers = range(1, n+1)
        while len(numbers) > 1:
            numbers = numbers[1::2]
            if len(numbers) == 1:
                return numbers[0]
            print numbers
            numbers = numbers[-2::-2]
            numbers = numbers[::-1]
            print numbers
        return numbers[0]


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        res = 1
        loop = 1
        while n > 1:
            res += loop
            loop *= 2
            n /= 2
            if n <= 1:
                return res
            if n % 2 == 1:
                res += loop
            loop *= 2
            n /= 2
        return res


if __name__ == "__main__":
    a = Solution()
    print a.lastRemaining(30)
    print a.lastRemaining(31)
    print a.lastRemaining(32)
    print a.lastRemaining(34)

