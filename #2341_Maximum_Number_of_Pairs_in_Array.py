class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _dict, count, rem = collections.Counter(nums), 0, 0
        for key, value in _dict.items():
            count += value//2
            rem += value%2
        return [count, rem]
