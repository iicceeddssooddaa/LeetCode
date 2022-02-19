class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        rem = nums[0]
        sto = [nums[0] == 0]
        for i in range(1, len(nums)):
            rem = (rem * 2 + nums[i])%5
            sto.append(rem %5 == 0)
        return sto
