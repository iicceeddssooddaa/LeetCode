class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # citations.sort()
        n = len(citations)
        if n <= citations[0]: return n
        left, right = 0, n - 1
        while left < right:
            mid = (left + right)//2
            if citations[mid - 1] <= n - mid <= citations[mid] : return n - mid
            elif n - mid > citations[mid]: left = mid + 1
            else: right = mid - 1
        if citations[left - 1] <= n - left <= citations[left] : return n - left
        else: return 0
