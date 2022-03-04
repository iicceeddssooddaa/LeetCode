class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = []
        for i in range(0,len(s),2):
            cache.append(s[i])
            if i + 1 < len(s): cache.append(chr(ord(s[i]) + int(s[i + 1])))
        string = "".join(cache)
        return string
