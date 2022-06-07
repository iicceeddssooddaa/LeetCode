class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        _dict = collections.Counter(num)
        for i in range(len(num)):
            if int(num[i]) != _dict[str(i)]: return False
        return True
