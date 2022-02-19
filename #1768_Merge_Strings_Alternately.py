class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, m, n, sto = 0, len(word1), len(word2), []
        for i in range(min(m,n)):
            sto.append(word1[i])
            sto.append(word2[i])
        if i < m - 1: sto.extend(word1[i+1:])
        if i < n - 1: sto.extend(word2[i+1:])
        string = "".join(sto)
        return string
