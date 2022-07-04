class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for i in range(n):
            if grid[i][i] * grid[i][-i-1] * grid[-i-1][i] * grid[-i-1][-i-1] == 0: return False
            if 2 * i + 1 == n:
                if sum(grid[j][i] for j in range(n)) - grid[i][i] != 0: return False
            elif sum(grid[j][i] for j in range(n)) - grid[i][i] - grid[-i-1][i] != 0: return False
        return True
