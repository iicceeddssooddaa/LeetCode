class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        while i <len(arr) - 2:
            if arr[i] * arr[i + 1] * arr[i + 2] & 1: return True
            else: i += 1
        return False
