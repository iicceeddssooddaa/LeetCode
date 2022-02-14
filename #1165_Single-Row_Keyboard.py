class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        _dict = {}
        for index,char in enumerate(keyboard):
            _dict[char] = index
        pos, dist = 0, 0
        for char in word:
            dist += abs(_dict[char] - pos)
            pos = _dict[char]
        return dist
