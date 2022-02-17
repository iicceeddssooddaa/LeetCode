class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        k, _list = 1, []
        _list.append(0)
        for i in range(1,n + 1):
            if i == 2**(k + 1): k += 1
            _list.append(_list[i - 2**k] + 1)
        return _list
