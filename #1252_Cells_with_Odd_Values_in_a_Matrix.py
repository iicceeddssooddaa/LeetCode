class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for index in indices:
            for i in range(n): matrix[index[0]][i] ^= 1
            for j in range(m): matrix[j][index[1]] ^= 1
        total = sum(sum(matrix[_][i] for i in range(n)) for _ in range(m))
        return total
