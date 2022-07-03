class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10 : return n
        
        def sumOfDigits(num):
            result = num%10
            while num > 9:
                num //=10
                result += num%10
            return result
        
        _dict, gp_ct, gp_sz = {}, 0, 0
        for i in range(n + 1):
            cache = sumOfDigits(i)
            if cache not in _dict: _dict[cache] = 1
            else: _dict[cache] += 1
            if _dict[cache] > gp_sz:
                gp_sz = _dict[cache]
                gp_ct = 1
            elif _dict[cache] == gp_sz:
                gp_ct += 1

        return gp_ct
