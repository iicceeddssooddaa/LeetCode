class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        profit, curmax = [0], 0
        for i in range(len(nums)-1): 
            profit.append(max(profit[i], 0) + nums[i + 1] - nums[i])
            if profit[-1] > curmax: curmax = profit[-1]
        return curmax if curmax >0 else -1
