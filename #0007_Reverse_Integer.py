class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = 1 if x > 0 else -1
        x *= sign
        List = []
        while x > 0:
            n = x%10
            x //= 10
            List.append(n)
        n = len(List)
        while List[-1] == 0:
            del List[-1]
        num = 0
        for n in range(len(List)):
            num *= 10
            num += List[n]
        num *= sign
        if num > 2**31 - 1 or num < -2**31:
            return 0
        return num
