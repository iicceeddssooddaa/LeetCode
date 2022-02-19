class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == "a": i += 1
            elif s[j] == "b": j -= 1
            else: break
        return i == j
-----------------
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]: return False
        return True
-----------------
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s
