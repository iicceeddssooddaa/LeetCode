class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        _dict = set(brokenLetters)
        word_list = text.split(" ")
        count = 0
        for word in word_list:
            cache = set(word)
            if len(cache.intersection(_dict)) == 0: count += 1
        return count
