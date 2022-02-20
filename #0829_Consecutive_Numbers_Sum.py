class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, count = int(sqrt(2 * n)), 0
        for i in range(1,x + 1):
            if (2*n) % i == 0 and (i + 2*n//i) % 2 != 0: count += 1
        return count
