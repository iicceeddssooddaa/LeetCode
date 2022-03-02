class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cache = deepcopy(heights)
        cache.sort()
        result = sum([cache[i] != heights[i] for i in range(len(heights))])
        return result
