class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k < arr[0]: return k
        cum = arr[0] - 1
        for i in range(1,len(arr)):
            if k - cum >= arr[i] - arr[i - 1]: 
                cum += arr[i] - arr[i - 1] - 1
            else: return arr[i - 1] + k - cum
        return arr[-1] + k - cum
