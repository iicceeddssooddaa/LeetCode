class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count1 = collections.Counter(magazine)
        count2 = collections.Counter(ransomNote)
        for key, value in count2.items():
            if key not in count1: return False
            if value > count1[key]: return False
        return True
