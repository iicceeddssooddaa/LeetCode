class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = collections.Counter(s)
        count_list = set(value for key,value in counter.items())
        return len(count_list) == 1
