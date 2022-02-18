class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sto, n = [nums[0]], len(nums)
        for i in range(1, n): sto.append(sto[-1] + nums[i])
        return sto
