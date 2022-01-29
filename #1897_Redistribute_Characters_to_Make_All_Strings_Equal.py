class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        _dict = {}
        for word in words:
            for char in word:
                if char not in _dict:
                    _dict[char] = 1
                else:
                    _dict[char] += 1
        n = len(words)
        for key, value in _dict.items():
            if value%n != 0:
                return False
        return True
