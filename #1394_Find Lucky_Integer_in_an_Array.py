class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = collections.Counter(arr)
        max_sto = -1
        for key, value in counter.items():
            if key == value: max_sto = max(key, max_sto)
        return max_sto
