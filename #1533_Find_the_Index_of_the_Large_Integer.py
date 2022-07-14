class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        n = reader.length()
        left, right, int_len = 0, n - 1, n//2
        while int_len >1:
            temp = reader.compareSub(left, left + int_len - 1, right - int_len + 1, right)
            if not temp: return left + int_len
            if temp == 1: right = left + int_len - 1
            else: left = right - int_len + 1
            int_len //=2
        temp = reader.compareSub(left,left,right,right)
        if not temp: return left + 1
