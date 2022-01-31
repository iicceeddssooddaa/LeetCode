class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        digits[:] = str(n)
        n_sum, n_prod = 0, 1
        for digit in digits:
            n_sum += int(digit)
            n_prod *= int(digit)
        return n_prod - n_sum
