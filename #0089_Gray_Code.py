class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        _list = [0, 1]
        if n == 1:
            return _list
        i = 1
        while i < n:
            addend = 2**i
            for j in range(2**i):
                _list.insert(addend, addend + _list[j])
            i += 1
        return _list
