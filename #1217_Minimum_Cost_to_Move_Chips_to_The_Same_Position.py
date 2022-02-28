class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        n = len(position)
        parity = sum(position[i] %2 for i in range(n))
        return min(parity, n - parity)
