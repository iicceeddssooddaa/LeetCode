class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        counter = collections.Counter(target)
        for num in arr:
            if num not in counter:
                return False
            counter[num] -= 1
            if counter[num] < 0:
                return False
        _set = {0}
        for value in counter.values():
            if value not in _set:
                return False
        return True
