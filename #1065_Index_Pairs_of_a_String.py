class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        sto = []
        for word in words:
            n = len(word)
            for i in range(len(text) - n + 1):
                if word[0] == text[i]:
                    if text[i:i + n] == word: sto.append([i, i + n - 1])
        sto.sort()
        return sto
