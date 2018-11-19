class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 0:
            return 0
        ret = 0
        minimum_price = prices[0]
        for i in range(1, length):
            if prices[i] > minimum_price:
                ret = max(ret, prices[i] - minimum_price)
            else:
                minimum_price = prices[i]
        return ret
