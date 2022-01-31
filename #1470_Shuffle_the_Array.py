class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_list = nums[n:]
        for i in range(n):
            new_list.insert(-2*i-1,nums[n - i - 1])
        return new_list
