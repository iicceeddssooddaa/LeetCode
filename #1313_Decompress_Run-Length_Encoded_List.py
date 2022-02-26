class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sto = []
        for i in range(0, len(nums), 2): sto.extend([nums[i + 1]] * nums[i])
        return sto
