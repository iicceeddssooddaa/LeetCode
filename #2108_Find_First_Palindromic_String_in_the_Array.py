class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word[-1::-1] == word: return word
        return ""
        # 折半检验会更快吗？但需要多一步算位置
