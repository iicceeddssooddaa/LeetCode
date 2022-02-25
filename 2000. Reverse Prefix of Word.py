class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word: return word
        j = 0
        while word[j] != ch: j += 1
        string = "".join(word[j::-1]) + "".join(word[j + 1:])
        return string
