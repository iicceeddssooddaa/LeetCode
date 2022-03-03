class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n, _dict = len(matrix), len(matrix[0]), {}
        for i in range(m):
            for j in range(n):
                if i - j not in _dict: _dict[i - j] = matrix[i][j]
                else: 
                    if matrix[i][j] != _dict[i - j]: return False
        return True
