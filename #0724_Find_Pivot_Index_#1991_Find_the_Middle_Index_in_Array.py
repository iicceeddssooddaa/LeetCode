class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        partial, n = [nums[0]], len(nums)
        for i in range(1, n): partial.append(partial[-1] + nums[i])
        total = partial[-1]
        if total == nums[0]: return 0
        for i in range(1, n): 
            if partial[i - 1] *2 == total - nums[i]: return i
        return -1
