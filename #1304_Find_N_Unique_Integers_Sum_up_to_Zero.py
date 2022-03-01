class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        if n%2 == 1:
            k = (n - 1)//2
            for i in range(-k,n - k): result.append(i)
        if n%2 == 0:
            k = n//2
            for i in range(1, k + 1): result.extend([-i, i])
        return result
