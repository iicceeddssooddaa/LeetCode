class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n, count = len(nums), 0
        for i in range(n):
            if nums[i] != val: count += 1
        i, j = 0, 0
        while i < count and j < n:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] = nums[j]
                    nums[j] = val
                    i += 1
            else:
                i += 1
            j += 1
        return count
