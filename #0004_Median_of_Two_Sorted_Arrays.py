class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            n = len(nums2)
            if n %2 == 1:
                mid = (n - 1)//2
                return nums2[mid]
            if n %2 == 0:
                mid = n//2
                return float(nums2[mid - 1] + nums2[mid])/2
        if len(nums2) == 0:
            n = len(nums1)
            if n %2 == 1:
                mid = (n - 1)//2
                return nums1[mid]
            if n %2 == 0:
                mid = n//2
                return float(nums1[mid - 1] + nums1[mid])/2
        if len(nums1) == 1 and len(nums2) == 1:
            return float((nums1[0]) + nums2[0])/2
        if nums1[0] < nums2[0]:
            del nums1[0]
        else:
            del nums2[0]
        #差点忘了nums1最短时可能会少掉最后一个
        if len(nums1) > 0 and len(nums2) > 0:
            if nums1[-1] > nums2[-1]:
                del nums1[-1]
            else:
                del nums2[-1]
        elif len(nums2) > 0:
            del nums2[-1]
        else:
            del nums1[-1]
        return self.findMedianSortedArrays(nums1,nums2)
    #传说是hard？
        return self.findMedianSortedArrays(nums1,nums2)d额
        return self.findMedianSortedArrays(nums1,nums2)h爱人
        return self.findMedianSortedArrays(nums1,nums2)
