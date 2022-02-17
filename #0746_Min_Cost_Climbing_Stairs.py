class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n < 3: return min(cost)
        frugal = [cost[0], cost[1]]
        for i in range(2,n): frugal[i%2] = cost[i] + min(frugal[(i - 1)%2], frugal[(i - 2)%2])
        return min(frugal)
