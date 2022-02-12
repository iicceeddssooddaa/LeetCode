class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 也就是找不大于目标的个数和小于目标的个数，用相等个数不等于0顺带判断存在。否则直接返回空。
        le, eq = 0, 0
        for i in range(len(nums)):
            if nums[i] < target: le += 1
            elif nums[i] == target: eq += 1
        if eq == 0: return []
        result = [le]
        for j in range(eq - 1):
            result.append(result[-1] + 1)
        return result
