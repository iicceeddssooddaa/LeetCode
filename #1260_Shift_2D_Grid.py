class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        k %= (m * n)
        if k == 0: return grid
        k1, k2 = k//n, k%n
        
        if k1:
            cache1 = grid[-k1:]
            cache2 = grid[:-k1]
            cache1.extend(cache2)
            grid = cache1
            
        if k2:
            cache = []
            for i in range(m):
                cache1 = grid[i-1][-k2:]
                cache2 = grid[i][:-k2]
                cache1.extend(cache2)
                cache.append(cache1)
            grid = cache
        return grid
