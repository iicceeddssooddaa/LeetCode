class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count, i = 0, 0
        while count < k and i < len(s):
            if s[i] != " ": i += 1
            elif s[i] == " " and count < k: 
                count += 1
                i += 1
        if count == k: return s[: i-1]
        if i == len(s): return s
