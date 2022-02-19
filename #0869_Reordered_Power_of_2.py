class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def powerOf2List(num):
            """
            :type num: int, number of digits
            :rtype: List[int], all power of 2 with certain number of digits
            Note at most 4 since a ten-fold could at most contain 4 of same digit powers. Time complexicty guaranteed.
            """
            i,sto = 0, []
            while 2 ** i  < 10 ** (num - 1): i += 1
            j = i
            while 2 ** j < 10 ** num: j += 1
            for k in range(i,j): sto.append(2**k)
            return sto
            
        check = powerOf2List(len(str(n)))
        _input = collections.Counter(str(n))
        for num in check:
            _output = collections.Counter(str(num))
            if _input == _output: return True
        return False
