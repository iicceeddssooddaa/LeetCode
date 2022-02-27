class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return nums[0] == 1
        def gcd(num1, num2):
            if num1 == num2: return num1
            if num1 < num2: num1, num2 = num2, num1
            while num2 != 0: num1, num2 = num2, num1%num2
            return num1
        cache = gcd(nums[-2], nums[-1])
        if cache == 1: return True
        for i in range(len(nums) - 2):
            cache = gcd(cache, nums[i])
            if cache == 1: return True
        return False
