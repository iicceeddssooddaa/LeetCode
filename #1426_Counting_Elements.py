class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = collections.Counter(arr)
        count = 0
        for key, value in counter.items():
            if key + 1 in counter: count += value
        return count
