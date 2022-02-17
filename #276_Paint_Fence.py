class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ways = [k**2, k]
        if n < 3: return ways[n%2]
        for i in range(3,n + 1):
            ways[i%2] = (ways[(i - 1)%2] + ways[(i - 2)%2])*(k - 1)
        return ways[n%2]
