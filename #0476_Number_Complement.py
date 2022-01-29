class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = []
        num_str[:] = "{0:b}".format(num)
        for i in range(len(num_str)):
            num_str[i] = 1 - int(num_str[i])
        res = 0
        for ele in num_str:
            res = (res << 1) | ele
        return res
