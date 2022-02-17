class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        def baserob(num):
            n = len(num)
            if n == 0: return 0
            if n < 3: return max(num)
            cache = max(num[0] + num[2], num[1])
            sto = [num[0],num[1],cache]
            for i in range(3,n):
                sto[i%3] = num[i] + max(sto[(i - 2)%3], sto[(i - 3)%3])
            return max(sto)

        return max(baserob(nums[:-1]), baserob(nums[1:]))
