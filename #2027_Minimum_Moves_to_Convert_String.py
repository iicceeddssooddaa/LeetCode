class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, i = 0, 0
        while i < len(s):
            if s[i] == "X":
                count += 1
                i += 3
            else: i += 1
        return count        
