class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sto, n = [nums[0]], len(nums)
        for i in range(1, n): self.sto.append(self.sto[-1] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0: return self.sto[right]
        return self.sto[right] - self.sto[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
