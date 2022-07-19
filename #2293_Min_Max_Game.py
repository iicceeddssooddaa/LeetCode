class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            temp = []
            for i in range(0, len(nums), 2):
                if i%4: temp.append(max(nums[i], nums[i + 1]))
                else: temp.append(min(nums[i], nums[i + 1]))
            nums = temp
        return nums[0]
