class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j, l0, l1 = 0, 1, 0, 0
        while j < len(s):
            if s[i] == s[j]: j += 1
            elif s[i] != s[j] and s[i] == s[j - 1]:
                if s[i] == "1": l1 = max(j - i, l1)
                if s[i] == "0": l0 = max(j - i, l0)
                i = j
                j += 1
        if s[i] == s[j - 1]:
            if s[i] == "1": l1 = max(j - i, l1)
            if s[i] == "0": l0 = max(j - i, l0)
        return l1 > l0        
