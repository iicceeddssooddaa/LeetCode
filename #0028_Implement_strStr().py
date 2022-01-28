class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        i = 0
        not_found = True
        while i < len(haystack) - len(needle) + 1 and not_found:
            if haystack[i] == needle[0]:
                not_found = not (haystack[i:i + len(needle)] == needle)
            i += 1
        return i - 1 if not_found == False else -1
