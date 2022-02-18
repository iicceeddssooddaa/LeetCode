class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        k = len(string)
        change = k - 1
        for i in range(k):
            if string[i] == "9": change -= 1
            else: break
        if change == -1: result = num
        else: result = num + 3 * (10 ** change)
        return result
