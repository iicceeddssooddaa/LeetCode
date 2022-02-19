class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos, n = 0, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]: 
                pos = i + 1
                break
        j, i, sort = pos, 0, True
        while i < n - 1 and sort:
            sort = nums[j % n] <= nums[(j + 1)%n]
            i += 1
            j += 1
        return sort
