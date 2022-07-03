class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1: return 0 if target == nums[0] else -1
        left, right = 0, len(nums) - 1
        while left < right:
            if target == nums[left]: return left
            if target == nums[right]: return right
            mid = (left + right)//2
            if target == nums[mid]: return mid
            if (nums[left] < target < nums[mid]) or (nums[mid] < nums[right] < nums[left] < target) or (target < nums[mid] < nums[right] < nums[left]): right = mid - 1
            else: left = mid + 1
        return left if target == nums[left] else -1
