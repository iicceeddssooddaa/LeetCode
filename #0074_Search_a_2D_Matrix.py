# 见过二分还试着写过，结果都没写下来。进步了进步了。
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        # search row number
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target: return True
            if matrix[mid][0] < target:
                if matrix[mid][right] < target: top = mid + 1
                else: 
                    top = mid
                    bottom = mid
            if matrix[mid][0] > target: bottom = mid - 1
        # search col number
        while left < right:
            center = (left + right) // 2
            if matrix[top][center] == target: return True
            if matrix[top][center] > target: right = center - 1
            if matrix[top][center] < target: left = center + 1
        return matrix[top][left] == target
