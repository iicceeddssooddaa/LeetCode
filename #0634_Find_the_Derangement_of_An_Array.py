class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        _list, mod = [1,0], 10**9 + 7
        for i in range(3,n + 1): _list[i%2] = (_list[(i - 1)%2] + _list[(i - 2)%2])*(i - 1) % mod
        return _list[n%2]
