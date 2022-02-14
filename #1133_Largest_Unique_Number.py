class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, unique = collections.Counter(nums), -1
        for key, value in counter.items():
            if value == 1: unique = max(unique, key)
        return unique
