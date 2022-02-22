class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # catalan number
        sto = 1
        for i in range(2, n + 1): 
            sto *= 4 * i  - 2
            sto //= (i + 1)
        return sto
