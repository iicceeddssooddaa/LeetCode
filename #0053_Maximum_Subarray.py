class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        temp_sum = [nums[0]]
        for i in range(1, len(nums)): temp_sum.append(max(0, temp_sum[-1]) + nums[i])
        return max(temp_sum)
