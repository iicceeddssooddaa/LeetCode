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
"""
USE 2, 4, 6 to check all posibilities:
    246, 264, 426, 462, 624, 642
    Among these 264, 426, 642 violate monotonicity so cross out.
    Let's see only cases where right side updated:
    1. 246. 2 < 4 so if in left half, it must be between.
    2. 462. Same.
    3. 624. Now it could be a 7 or a 1. So then mid < right < left immediately. And the extra is that target is the smallest or largets.
    Therefore we obtained the huge if condition.
"""
