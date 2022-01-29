class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return [10,1][n%2]
        count, i = 10, 2
        while i <= n:
            perm = 1
            for j in range(9, 10 - i, -1):
                perm *= j
            count += 9 * perm
            i += 1
        return count
      #nth increment = 9 * 9 * \cdots * (11 - n)
