class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        char_set, count = set(allowed), 0
        for word in words: count += 1 if set(word).issubset(char_set) else 0
        return count
