class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sto = []
        for i in range(len(matrix)):
            self.sto.append([matrix[i][0]])
            for j in range(1, len(matrix[0])):
                self.sto[i].append(self.sto[i][j - 1] + matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 == 0: cache = sum(self.sto[i][col2] for i in range(row1, row2 + 1))
        else: cache = sum(self.sto[i][col2] - self.sto[i][col1 - 1] for i in range(row1, row2 + 1))
        return cache


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
