class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        for interval in intervals: interval[1] *= -1
        intervals.sort()
        for interval in intervals: interval[1] *= -1
        count, curmax = 1, intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][1] > curmax:
                curmax = intervals[i][1]
                count += 1
        return count
