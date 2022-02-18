class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if perfect square of a prime
        if n < 4: return False
        x = int(sqrt(n))
        if x**2 != n : return False
        for i in range(2,(x + 1)//2): if x % i == 0: return False
        return True
