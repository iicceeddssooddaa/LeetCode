class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words, vowel, sto = sentence.split(" "), set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']), []
        for index, word in enumerate(words):
            if word[0] in vowel: sto.append(word + "m" + "a"*(index + 2))
            else: sto.append(word[1:] + word[0] + "m" + "a"*(index + 2))
        string = " ".join(sto)
        return string
