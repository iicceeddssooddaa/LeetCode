#参考892的思路来的
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        zero_list = [0]*(n + 2)
        for i in range(m):
            grid[i].append(0)
            grid[i].insert(0,0)
        grid.append(zero_list)
        grid.insert(0, zero_list)
       
        for i in range(m + 1):
            bw_rows = sum([abs(grid[i][j] - grid[i + 1][j]) for j in range(n + 1)])
            within_rows = sum(abs(grid[i][j] - grid[i][j + 1]) for j in range(n + 1))
            perimeter += bw_rows + within_rows
        return perimeter
