class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum_max, temp_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]: temp_sum = temp_sum + nums[i]
            else: temp_sum = nums[i]
            if temp_sum > cum_max: cum_max = temp_sum
        return cum_max
