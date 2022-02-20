class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def secondSmallestDivisor(n):
            if n < 6: return 0
            x = int(sqrt(n))
            if x ** 2 == n: return 0
            cache = []
            for i in range(2, x + 1):
                if n % i == 0:
                    if len(cache) == 0: cache.append(i)
                    else: return 0
            return 0 if len(cache) == 0 else cache[0]
        
        cache = 0
        for num in nums:
            temp = secondSmallestDivisor(num)
            if bool(temp):
                cache += (1 + num + temp + num//temp)
        return cache
