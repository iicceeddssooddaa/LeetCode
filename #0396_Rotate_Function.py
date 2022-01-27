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
    
--------------#对比冯老师的写法（下）：
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, s = len(nums), sum(nums)
        
        F = sum([i * nums[i] for i in range(n)])
        res = float("-Inf")
        
        for i in range(n):
            res = max(res, F)
            F += s - n * nums[n-1-i]
        
        return res
