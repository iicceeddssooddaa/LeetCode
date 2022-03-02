class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = [(prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0) for i in range(1, len(prices))]
        return sum(profit)
