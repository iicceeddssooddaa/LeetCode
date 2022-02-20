class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        n = len(arr)
        arr.sort()
        print arr
        cut = n//20
        del arr[:cut]
        del arr[-1*cut:]
        average = float(sum(arr))/len(arr)
        return average
