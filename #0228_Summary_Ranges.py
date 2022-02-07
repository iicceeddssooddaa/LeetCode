class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]
        result, i, pos, head = [], 0, 1, nums[0]
        while i < n - 1:
            if nums[i] + 1 == nums[i + 1]:
                pos += 1
            elif pos == 1:
                result.append(str(nums[i]))
                head = nums[i + 1]
            elif nums[i] + 1 < nums[i + 1]:
                pos = 1
                result.append(str(head) + "->" + str(nums[i]))
                head = nums[i + 1]
            i += 1
        if pos == 1:
            result.append(str(nums[-1]))
        else: 
            result.append(str(head) + "->" + str(nums[i]))
        return result
