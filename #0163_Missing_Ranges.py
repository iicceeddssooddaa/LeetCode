class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        result = []
        if n == 0:
            if lower == upper: return [str(lower)]
            else: return[str(lower)+"->"+str(upper)]
        if nums[0] > lower + 1:
            result.append(str(lower)+"->"+str(nums[0] - 1))
        if nums[0] == lower + 1:
            result.append(str(lower))
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 2:
                result.append(str(nums[i] + 1))
            if nums[i + 1] - nums[i] > 2:
                result.append(str(nums[i] + 1)+"->"+str(nums[i + 1] - 1))
        if nums[-1] + 1 == upper:
            result.append(str(upper))
        if nums[-1] + 1 < upper:
            result.append(str(nums[-1] + 1)+"->"+str(upper))
        return result
