class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        _list = [[]]
        for i in range(len(nums)):
            for j in range(len(_list)):
                cache = []
                cache[:] = _list[j]
                cache.append(nums[i])
                _list.append(cache)
        return _list
