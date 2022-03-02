class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i%10 != nums[i]: i += 1
            else: break
        return i if i < len(nums) else -1
--------------
class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sto = [(nums[i] == i%10) for i in range(len(nums))]
        return -1 if 1 not in sto else sto.index(1) 
