class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n <= nums[0]: return n
        left, right = 0, n - 1
        while left < right:
            mid = (left + right + 1)//2
            if nums[mid - 1] < n - mid <= nums[mid]: return n - mid
            elif n - mid > nums[mid]: left = mid + 1
            else: right = mid - 1
        if nums[left - 1] < n - left <= nums[left]: return n - left
        else: return -1
