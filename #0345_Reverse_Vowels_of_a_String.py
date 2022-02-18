class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sto = []
        sto[:] = s
        vowel = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])
        i, j = 0, len(sto) - 1
        while i < j:
            if sto[i] not in vowel: i += 1
            elif sto[j] not in vowel: j -= 1
            else: 
                sto[i], sto[j] = sto[j], sto[i]
                i += 1
                j -= 1
        string = "".join(sto)
        return string
