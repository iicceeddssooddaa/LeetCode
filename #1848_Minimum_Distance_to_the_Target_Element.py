class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        if nums[start] == target: return 0
        temp = len(nums)
        for index, num in enumerate(nums):
            if num == target: temp = min(abs(index - start), temp)
        return temp
