class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1 + (sqrt(8 * n -7) - 1)/2
        return int(x)
# (k + 1)k/2 <= n - 1 求正根下最大整数
