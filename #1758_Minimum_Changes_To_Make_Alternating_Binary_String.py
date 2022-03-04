class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, n = 0, len(s)
        for i in range(n): count += ((i%2) == int(s[i]))
        return min(count, n - count)
