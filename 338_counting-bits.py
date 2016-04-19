class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(1, num + 1):
            if i % 2 == 1:
                result[i] = result[i/2] + 1
            else:
                result[i] = result[i/2]
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
