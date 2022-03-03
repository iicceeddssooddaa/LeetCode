class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        new = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        return new
