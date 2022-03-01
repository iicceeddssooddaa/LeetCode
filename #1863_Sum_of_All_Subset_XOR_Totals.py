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
----------------
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, total = [0], 0
        for num in nums:
            n = len(result)
            for i in range(n): 
                cache = num ^ result[i]
                result.append(num ^ result[i])
                total += cache
        return total
