class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = []
        for i in range(0,len(s)-1,2):
            cache.extend([s[i], chr(ord(s[i]) + int(s[i + 1]))])
        if len(s)%2 == 1: cache.append(s[-1])
        string = "".join(cache)
        return string
