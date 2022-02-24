class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n, total = len(mat), 0
        for i in range(n): total += mat[i][i] + mat[i][n - i - 1]
        if n %2 != 0: total -= mat[n//2][n//2]
        return total
