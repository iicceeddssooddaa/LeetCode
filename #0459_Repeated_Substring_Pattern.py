class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        i, n = 0, len(s)
        while i < n - 1:
            if s[:n - i - 1] == s[i + 1:] and n%(i+1) == 0:
                return True
            i += 1
        return False
