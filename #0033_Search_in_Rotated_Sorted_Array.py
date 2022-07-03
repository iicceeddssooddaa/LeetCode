class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1: return 0 if target == nums[0] else -1
        # search for position of min of the list
        if nums[-1] < nums[-2]:
            left, right = len(nums) - 1, len(nums) - 1
        elif nums[0] > nums[1]:
            left, right = 1, 1
        elif nums[0] < nums[-1]:
            left, right = 0, 0
        else:
            left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[0] > nums[mid]:
                right = mid
            elif nums[0] < nums[mid]:
                left = mid + 1
            else:
                left, right = mid, mid
        # search the half it belongs to
        if target == nums[0]: return 0
        elif target < nums[0]: right = len(nums) - 1
        elif left == 0:
             right = len(nums) - 1
        else: left, right = 0, right - 1
        if target == nums[left]: return left
        if target == nums[right]: return right
        while left < right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else: left, right = mid, mid
        return left if target == nums[left] else -1
