class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return [19,3,8][n%3]
        x, y, mod = [1,2,4,7], ['-inf', 1,4,12], 10**9 + 7
        for i in range(4, n + 1):
            x[i%4] = (x[(i - 1)%4] + x[(i - 2)%4] + x[(i - 3)%4]) % mod
            y[i%4] = (x[i%4] + y[(i - 1)%4] + y[(i - 2)%4] + y[(i - 3)%4]) % mod
        return (x[n%4] + y[n%4]) % mod
