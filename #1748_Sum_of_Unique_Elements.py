class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, _dict = 0, {}
        for num in nums:
            if num not in _dict:
                result += num
                _dict[num] = 1
            elif _dict[num] == 1:
                result -= num
                _dict[num] += 1
        return result
----------
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, _dict = 0, {}
        _dict = collections.Counter(nums)
        for key, value in _dict.items():
            if value == 1: result += key
        return result
