class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcpPair(str1, str2):
            i = 0
            while i < len(str1) and i < len(str2):
                if str1[i] == str2[i]: i += 1
                else: break
            return str1[:i]
        cache = strs[-1]
        for i in range(len(strs) - 1): cache = lcpPair(strs[i], cache)
        return cache
