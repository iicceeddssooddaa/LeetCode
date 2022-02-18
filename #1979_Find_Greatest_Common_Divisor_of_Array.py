class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_max, arr_min = 0, 1001
        for num in nums: arr_max, arr_min = max(arr_max, num), min(arr_min, num)
        # find GCD next
        while arr_min != 0: arr_max, arr_min = arr_min, arr_max % arr_min
        return arr_max
