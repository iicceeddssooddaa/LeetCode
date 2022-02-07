class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rec, length = [], []
        n = len(s)
        if n == 1:
            return s
        for i in range(n - 2):
            if s[i] == s[i + 1]: rec.append([i,i + 1])
            if s[i] == s[i + 2]: rec.append([i,i + 2])
        if s[-2] == s[-1]: rec.append([n - 2, n - 1])
        # 构造对称核。而后增长所有的核。
        for sub in rec:
            stop = True
            while sub[0] > 0 and sub[1] < n - 1 and stop:
                if s[sub[0] - 1] == s[sub[1] + 1]:
                    sub[0] -= 1
                    sub[1] += 1
                else:
                    stop = False
            length.append(sub[1] - sub[0] + 1)
        # 特殊情况，已然排除单长度，若无非平凡回文子序列，返回第一个平凡字符
        if len(length) == 0:
            return s[0]
        longest = max(length)
        i = 0
        # 回复第一个最长
        while length[i] < longest:
            i += 1
        return s[rec[i][0]:rec[i][1]+1]
