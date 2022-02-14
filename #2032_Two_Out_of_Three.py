class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        # 第一次记出现。第二次识别在第一次中是否出现再存储。第三次判断是否包含即可存储。
        result, count, sto = set(), {}, []
        for num in nums1:
            if num not in count: count[num] = 1
        for num in nums2:
            if num not in count: count[num] = 2
            elif count[num] == 1: result.add(num)
        for num in nums3:
            if num in count: result.add(num)
        sto[:] = result
        return sto
