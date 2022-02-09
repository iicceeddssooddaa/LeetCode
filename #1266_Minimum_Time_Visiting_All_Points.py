class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 1:
            return 0
        time  = 0
        # 取坐标差绝对值。尽量沿对角线移动，即差向量取较小。而后沿单向移动，取两者差的绝对值
        for i in range(n - 1):
            diffx = abs(points[i][0] - points[i + 1][0])
            diffy = abs(points[i][1] - points[i + 1][1])
            time += min(diffx, diffy) + abs(diffx - diffy)
        return time
