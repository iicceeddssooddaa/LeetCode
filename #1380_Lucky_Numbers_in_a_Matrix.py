class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        _dict, cache, result = {}, set(), []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            temp, pos = "inf", -1
            for j in range(n):
                if matrix[i][j] < temp:
                    temp = matrix[i][j]
                    pos = j
            cache.add(pos)
            if pos not in _dict: _dict[pos] = [temp]
            else: _dict[pos].append(temp)
        for j in cache:
            temp = float("-inf")
            for i in range(m):
                if matrix[i][j] > temp: temp = matrix[i][j]
            if temp in _dict[j]: result.append(temp)
        return result
