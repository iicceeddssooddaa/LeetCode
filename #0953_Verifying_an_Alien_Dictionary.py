class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) == 1: return True
        _dict, cache = {}, []
        for i in range(0,26):
            _dict[order[i]] = chr(i+97)
        for char in words[0]:
            cache.append(_dict[char])
        prevword = "".join(cache)
        for i in range(1,len(words)):
            cache = []
            for char in words[i]:
                cache.append(_dict[char])
            nextword = "".join(cache)
            if prevword > nextword: return False
            else: prevword = nextword
        return True
