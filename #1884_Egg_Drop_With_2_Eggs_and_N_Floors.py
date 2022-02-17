class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1 + (sqrt(8 * n -7) - 1)/2
        return int(x)
