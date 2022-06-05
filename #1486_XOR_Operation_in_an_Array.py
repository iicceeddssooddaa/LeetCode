class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        cache1, cache2 = start, start
        for i in range(1, n):
            cache1 += 2
            cache2 ^= cache1
        return cache2
