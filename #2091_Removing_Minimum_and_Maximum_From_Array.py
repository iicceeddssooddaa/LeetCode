class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high, low, high_pos, low_pos = float('-inf'), float('inf'),0,0
        for index, value in enumerate(nums):
            if value > high: 
                high = value
                high_pos = index
            if value < low:
                low = value
                low_pos = index
        move = min(max(high_pos, low_pos) + 1, high_pos + 1 + len(nums) - low_pos, low_pos + 1 + len(nums) - high_pos, len(nums) - min(high_pos, low_pos))
        return move
