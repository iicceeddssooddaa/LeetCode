class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n == 2: return True
        arr.sort(reverse = True)
        diff = arr[0] - arr[1]
        for i in range(n - 2):
            if arr[i + 1] - arr[i + 2] != diff: return False
        return True
