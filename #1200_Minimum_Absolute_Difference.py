class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        sto, min_diff = [], "inf"
        arr.sort()
        for i in range(len(arr) - 1): min_diff = min(min_diff, arr[i + 1] - arr[i])
        for i in range(len(arr) - 1): 
            if arr[i + 1] - arr[i] == min_diff: sto.append([arr[i], arr[i + 1]])
        return sto
