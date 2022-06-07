class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        set_cov = set()
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                set_cov.add(i)
        for i in range(left, right + 1):
            if i not in set_cov: return False
        return True
---------
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        n = len(ranges)
        for i in range(left, right + 1):
            j = 0
            not_covered = True
            while j < n and not_covered:
                if ranges[j][0] <= i <= ranges[j][1]: not_covered = False
                j += 1
            if not_covered: return False
        return True
