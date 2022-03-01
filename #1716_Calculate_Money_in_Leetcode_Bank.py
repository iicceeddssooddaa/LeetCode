class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        w, d = n//7, n%7
        result = 7 * w * (w + 1)//2 + w*(21 + d) + d * (d + 1) // 2
        return result
