class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        rem, new = numBottles % numExchange, numBottles // numExchange
        total, numBottles = rem + new, numBottles + new
        while total >= numExchange:
            rem, new = total % numExchange, total // numExchange
            total, numBottles = rem + new, numBottles + new
        return numBottles
