class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] < i:
                i += 1
            elif arr[i] == i:
                return i
            else:
                break
        return -1
