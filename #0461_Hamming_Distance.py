class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:].zfill(32)
        y_bin = bin(y)[2:].zfill(32)
        count = 0
        for i in range(32):
            count += 1 if int(x_bin[i]) ^ int(y_bin[i]) else 0
        return count
