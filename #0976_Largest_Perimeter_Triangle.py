class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        i = 0
        while i < len(nums) - 3:
            if nums[i] >= nums[i + 1] + nums[i + 2]: i += 1
            else: break
        if i < len(nums) - 3: return nums[i] + nums[i + 1] + nums[i + 2]
        else: return 0 if nums[i] >= nums[i + 1] + nums[i + 2] else nums[i] + nums[i + 1] + nums[i + 2]
