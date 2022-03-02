class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        cur_max, sto = arr[-1], deque([-1])
        for i in range(len(arr) - 2, -1, -1):
            sto.appendleft(cur_max)
            if arr[i] > cur_max: cur_max = arr[i]
        return sto
