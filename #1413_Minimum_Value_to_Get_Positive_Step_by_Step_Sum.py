class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        partial, small = nums[0], nums[0]
        for i in range(1, len(nums)):
            partial = nums[i] + partial
            small = min(small, partial)
        return 1 - small if small <0 else 1
