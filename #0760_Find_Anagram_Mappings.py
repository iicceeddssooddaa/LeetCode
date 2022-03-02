class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _dict, sto = {}, []
        for index, num in enumerate(nums2): _dict[num] = index
        for num in nums1: sto.append(_dict[num])
        return sto
