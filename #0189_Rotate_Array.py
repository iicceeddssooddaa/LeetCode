class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return nums
        cache_list = nums[:-k]
        del nums[:-k]
        nums.extend(cache_list)
        没有O(1)
----------
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return nums
        nums[:k], nums[k:] = nums[-k:], nums[:-k] 
-------------
if k%len(nums) == 0: return nums
        nums[:k % len(nums)], nums[k % len(nums):] = nums[-(k % len(nums)):], nums[:-(k % len(nums))] 
