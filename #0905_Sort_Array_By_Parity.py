class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[i] %2 == 0: i += 1
            elif nums[j] %2 != 0: j -= 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums
