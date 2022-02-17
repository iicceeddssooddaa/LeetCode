class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return [1,2,3][n]
        x, k, fib = "{0:b}".format(n), len(x) - 1, [2,1,1]
        for i in range(4, k + 3): fib[i%3] = fib[(i - 1)%3] + fib[(i - 2)%3]
        if n * 2/3 >= 2**k: return fib[(k + 2)%3] + fib[(k + 1)%3]
        else: return fib[(k + 2)%3] + self.findIntegers(n - 2**k)
