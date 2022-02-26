class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        sto = []
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y: sto.append([abs(point[0] - x) + abs(point[1]- y), index])
        sto.sort()
        return -1 if len(sto) == 0 else sto[0][1]
