class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, curmax = [0], 0
        for i in range(len(prices)-1): 
            profit.append(max(profit[i], 0) + prices[i + 1] - prices[i])
            if profit[-1] > curmax: curmax = profit[-1]
        return curmax
