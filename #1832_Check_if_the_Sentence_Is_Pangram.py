class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26: return False
        _dict = set(sentence)
        return len(_dict) ==  26
