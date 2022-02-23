class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, count = len(grid), len(grid[0]), 0
        i, j = m - 1, 0
        while i >= 0 and j < n:
                if grid[i][j] >= 0: j += 1
                elif grid[i][j] < 0: 
                    count += n - j
                    i -= 1
        return count
