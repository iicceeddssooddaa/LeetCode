class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 1: return triangle[0][0]
        cache = triangle[-1]
        for j in range(1, n):
            for i in range(n - j): cache[i] = triangle[n - j - 1][i] + min(cache[i], cache[i + 1])
        return cache[0]
