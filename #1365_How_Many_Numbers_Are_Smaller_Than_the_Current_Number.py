class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_c, _dict, result = deepcopy(nums), {}, []
        nums_c.sort()
        for i in range(len(nums_c) - 1, 0, -1):
            if nums_c[i]>nums_c[i - 1]: _dict[nums_c[i]] = i
        if nums_c[0] not in _dict: _dict[nums_c[0]] = 0
        for i in range(len(nums)): result.append(_dict[nums[i]])
        return result
