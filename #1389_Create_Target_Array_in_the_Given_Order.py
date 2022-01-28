class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        _list = []
        i = 0
        while i < len(nums):
            _list.insert(index[i], nums[i])
            i += 1
        return _list
        #可能是练习用的
