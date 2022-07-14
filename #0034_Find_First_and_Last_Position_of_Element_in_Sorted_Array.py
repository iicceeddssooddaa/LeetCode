class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []: return [-1,-1]
        if target == nums[0]: l_end, left = 0, 0
        else:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right)//2
                if nums[mid] >= target: right = mid
                else: left = mid + 1
            if target != nums[left]: return [-1,-1]
            l_end = left
        if target == nums[-1]: r_end = len(nums) - 1
        else:
            right = len(nums) - 1
            while left < right:
                mid = (left + right + 1)//2
                if nums[mid] <= target: left = mid
                else: right = mid - 1
            r_end = right
        return [l_end, r_end]
