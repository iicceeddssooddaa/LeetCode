class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i%10 != nums[i]: i += 1
            else: break
        return i if i < len(nums) else -1
