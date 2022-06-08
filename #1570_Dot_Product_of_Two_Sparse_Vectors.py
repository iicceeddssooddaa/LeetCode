class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indset, self.dict = set(), {}
        for i in range(len(nums)):
            if nums[i] != 0: 
                self.indset.add(i)
                self.dict[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res, com_index = 0, self.indset.intersection(vec.indset)
        for key in com_index:
            res += self.dict[key] * vec.dict[key]
        return res
