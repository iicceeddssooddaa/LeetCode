class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        if n == 1: return [char for char in words[0]]
        _dict, sto = collections.Counter(words[0]), []
        for i in range(1,n):
            cache = collections.Counter(words[i])
            for key, value in _dict.items(): _dict[key] = min(value, cache[key])
        for key, value in _dict.items(): sto.extend([key]*value)
        return sto
