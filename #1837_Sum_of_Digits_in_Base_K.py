class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sto = n % k
        n //= k
        while n > 0:
            sto += n%k
            n //= k
        return sto
