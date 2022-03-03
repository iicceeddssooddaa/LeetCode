class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        i, j, sto = 0, 1, []
        while j < len(s):
            if s[i] == s[j]: pass
            else:
                if s[i] == s[j - 1] and j - i >= 3: sto.append([i,j - 1])
                i = j
            j += 1
        if s[i] == s[-1] and j - i >= 3: sto.append([i, j - 1])
        return  sto
