class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3: return False
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] < arr[i + 1]: i += 1
            elif arr[j] < arr[j - 1]: j -= 1
            else: break
        return i == j and i > 0 and j < len(arr) - 1
