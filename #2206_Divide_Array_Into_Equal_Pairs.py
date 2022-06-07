class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _dict = collections.Counter(nums)
        for key, value in _dict.items():
            if value %2 !=0 : return False
        return True
-----------
        seen = set()
        for n in nums:
            seen ^= {n}
        return not seen
