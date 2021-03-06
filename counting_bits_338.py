"""
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's 
in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? 
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Solution2 is better
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(1, num + 1):
            if i % 2 == 1:
                result[i] = result[i / 2] + 1
            else:
                result[i] = result[i / 2]
        return result


class Solution2(object):
    def countBits(self, num):
        result = [0] * (num + 1)
        for i in xrange(0, (num + 1) / 2):
            result[2 * i] = result[i]
            result[2 * i + 1] = result[i] + 1
        if num % 2 == 1:
            result[num] = result[num / 2] + 1
        else:
            result[num] = result[num / 2]
        return result
