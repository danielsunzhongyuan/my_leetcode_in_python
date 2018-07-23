class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # length = len(prices)
        # if length <= 1:
        #     return 0
        # ret = 0
        # i, j = 0, 0
        # while i < length:
        #     while j < length - 1 and prices[j+1] > prices[j]:
        #         j += 1
        #     ret += prices[j] - prices[i]
        #     i = j + 1
        #     j = j + 1
        # return ret
        
        length = len(prices)
        if length <= 1:
            return 0
        ret = 0
        for i in range(1, length):
            if prices[i] - prices[i-1] > 0:
                ret += prices[i] - prices[i-1]
        return ret
