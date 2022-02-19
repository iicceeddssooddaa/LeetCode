class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2): return False
        n = len(sentence1)
        for i in range(n):
            if sentence1[i] != sentence2[i] and ([sentence1[i], sentence2[i]] not in similarPairs) and ([sentence2[i], sentence1[i]] not in similarPairs): return False
        return True
