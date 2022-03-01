class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0]
        for num in nums:
            n = len(result)
            for i in range(n): result.append(num ^ result[i])
        return sum(result)
