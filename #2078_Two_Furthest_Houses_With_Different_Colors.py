class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n, left, right = len(colors), 0, len(colors) - 1
        while colors[left] == colors[-1]: left += 1
        while colors[right] == colors[0]: right -= 1
        return max(right, n - 1 - left)
