class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        count = 0
        for key, value in counter.items():
            count += value * (value + 1) //2
        return count
        #就这？
