class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        small, big = float("inf"), float("-inf")
        for num in nums:
            small = num if num < small else small
            big = num if num > big else big
        result = max(0, big - small - 2*k)
        return result
