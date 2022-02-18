class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        string = str(n)
        k = len(string)
        for i in range(k): n -= int(string[i])**k
        return n == 0
