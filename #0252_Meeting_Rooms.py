class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        for interval in intervals: interval[1] *= -1
        intervals.sort()
        for interval in intervals: interval[1] *= -1
        cache = [-1, -1]
        for i in range(len(intervals)):
            if intervals[i][0] >= cache[1]: cache = intervals[i]
            else: return False
        return True
