class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1, pos2 = [], []
        for pos,word in enumerate(wordsDict):
            if word == word1:
                pos1.append(pos)
            if word == word2:
                pos2.append(pos)
        dist = []
        if len(pos1) == 1:
            return min([abs(item - pos1[0]) for item in pos2])
        if len(pos2) == 1:
            return min([abs(item - pos2[0]) for item in pos1])
        i, j = 0, 0
        while i < len(pos1) and j < len(pos2):
            if pos1[i] < pos2[j]:
                dist.append(pos2[j] - pos1[i])
                i += 1
            elif pos2[j] < pos1[i]:
                dist.append(pos1[i] - pos2[j])
                j += 1
        return min(dist)
