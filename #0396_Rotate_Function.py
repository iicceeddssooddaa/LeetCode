class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        _sum = sum(nums)
        maxF = 0
        for i in range(len(nums)):
            maxF += i * nums[i]
        nextF = maxF
        for i in range(1,len(nums)):
            nextF += _sum - n * nums[-i]
            maxF = max(maxF, nextF)
        return maxF
