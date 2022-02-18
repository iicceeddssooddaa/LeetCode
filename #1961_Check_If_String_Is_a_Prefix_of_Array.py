class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        # is_prefix 为默认真值， i为滚动检查的词条序数，cum为累计至此已检查过的字符串长度
        is_prefix, i, cum = True, 0, 0
        while is_prefix and i < len(words) and cum < len(s):
            p = len(words[i])
            if len(s[cum:]) < p: 
                is_prefix = False # 需保留，极大提高速度
                break
            else:
                is_prefix = s[cum: cum + p] == words[i]
                cum += len(words[i])
                i += 1
        return is_prefix and cum == len(s) and i <= len(words)
