class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m - 1
        while j >=0:
            if matrix[j][0] > target: j -= 1
            else: break
        if j == -1: return False
        while i < n: 
            if matrix[j][i] < target: i += 1
            else: break
        if i == n: return False
        return matrix[j][i] == target
