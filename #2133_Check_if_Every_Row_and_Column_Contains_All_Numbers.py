class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            cache1, cache2 = [1] * n, [1] *n
            for j in range(n):
                cache1[matrix[i][j] - 1] -= 1
                cache2[matrix[j][i] - 1] -= 1
                if cache1[matrix[i][j] - 1] < 0 or cache2[matrix[j][i] - 1] < 0: return False
        return True
