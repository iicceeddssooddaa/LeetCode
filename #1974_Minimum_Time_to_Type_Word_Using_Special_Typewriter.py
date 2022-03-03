class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        _dict= {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        dist = 1 + min(_dict[word[0]], 26 - _dict[word[0]])
        for i in range(1, len(word)): dist += min(abs(_dict[word[i]] - _dict[word[i - 1]]), abs(_dict[word[i]] + 26 - _dict[word[i - 1]]), abs(_dict[word[i]] - 26 - _dict[word[i - 1]])) + 1
        return dist
