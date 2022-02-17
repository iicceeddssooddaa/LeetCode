class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n < 3: return max(nums)
        cache = max(nums[0] + nums[2], nums[1])
        sto = [nums[0],nums[1],cache]
        for i in range(3,n): sto[i%3] = nums[i] + max(sto[(i - 2)%3], sto[(i - 3)%3])
        return max(sto)
