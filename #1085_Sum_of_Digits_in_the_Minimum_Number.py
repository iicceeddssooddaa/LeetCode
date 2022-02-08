class Solution(object):
    def sumOfDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ele = "inf"
        for i in range(len(nums)):
            min_ele = min(min_ele, nums[i])
        result = min_ele//10 + min_ele%10
        return int(result %2 == 0)
      #思考：最小值需要遍历。因而复杂度难以降低？
