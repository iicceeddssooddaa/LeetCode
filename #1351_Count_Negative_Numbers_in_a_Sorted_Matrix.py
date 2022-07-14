class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, count, left = len(grid), len(grid[0]), 0, 0
        for i in range(m - 1, -1, -1):
            right = n - 1
            if grid[i][left] < 0: 
                count += n - left
                continue
            elif grid[i][right] >= 0: return count
            else:
                while left < right:
                    mid = (left + right)//2
                    if grid[i][mid] >= 0 > grid[i][mid + 1]:
                        left, right = mid + 1, mid + 1
                    elif grid[i][mid] < 0: right = mid
                    else: left = mid + 1
                count += n - left
        return count
