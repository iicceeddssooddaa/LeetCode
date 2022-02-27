class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n, i, string = len(sequence), 1, word
        while string in sequence:
            i += 1
            string = word * i
        return i - 1
