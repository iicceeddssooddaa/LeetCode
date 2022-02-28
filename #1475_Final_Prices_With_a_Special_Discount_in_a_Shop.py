class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        sto, cache_min = [prices[-1]], prices[-1]
        for j in reversed(range(len(prices) - 1)):
            if prices[j] < cache_min: 
                cache_min = prices[j]
                sto.insert(0,prices[j])
            else: 
                i = j + 1
                while prices[j] < prices[i]: i += 1
                sto.insert(0,prices[j] - prices[i])
        return sto
