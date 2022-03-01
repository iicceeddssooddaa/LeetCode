class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sto, _dict = [], {}
        for index, num in enumerate(nums2): _dict[num] = index
        for i in range(len(nums1)):
            j = _dict[nums1[i]]
            while j < len(nums2) and nums1[i] >= nums2[j]: j += 1
            if j == len(nums2): sto.append(-1)
            else: sto.append(nums2[j])
        return sto
