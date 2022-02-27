class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        for interval in intervals: interval[1] *= -1
        intervals.sort()
        for interval in intervals: interval[1] *= -1
        stack = []
        for i in range(len(intervals)):
            if len(stack) == 0: stack.append(intervals[i])
            if intervals[i][0] <= stack[-1][1]: stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else: stack.append(intervals[i])
        return stack
