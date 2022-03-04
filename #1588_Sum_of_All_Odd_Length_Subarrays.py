class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total, n = 0, len(arr)
        for length in range(1,n + 1,2):
            for i in range(n - length + 1):
                total += sum(arr[i:i + length])
        return total
