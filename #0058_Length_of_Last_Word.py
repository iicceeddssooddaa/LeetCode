class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        _list = [item for item in s.split(" ") if item]
        return len(_list[-1])
