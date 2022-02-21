class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base-9 conversion
        cache = [n % 9]
        n //= 9
        while n > 0:
            cache.insert(0,n%9)
            n//=9
        result = cache[0]
        for i in range(1,len(cache)):
            result *= 10
            result += cache[i]
        return result
