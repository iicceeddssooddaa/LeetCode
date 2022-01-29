class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_dict = {}
        for pos,num in enumerate(nums):
            if num not in pos_dict:
                pos_dict[num] = 1
            else:
                pos_dict[num] += 1
        count = 0
        for key, value in pos_dict.items():
            count += value * (value - 1) // 2
        return count
