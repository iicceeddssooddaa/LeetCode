class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sto = []
        vowel = set(["a", "e", "i", "o", "u"])
        for char in s:
            if char not in vowel: sto.append(char)
        string = "".join(sto)
        return string
