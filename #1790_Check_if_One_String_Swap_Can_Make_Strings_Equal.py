class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 预判断长度。对不同位记录分别记录两个字符。检查字典长度为0或2，为2追加判断字符对调。
        n, _dict = len(s1), {}
        if len(s2) != n: return False
        for i in range(n): 
            if s1[i] != s2[i]: _dict[i] = [s1[i], s2[i]]
        if len(_dict) ==0: return True
        elif len(_dict) !=2: return False
        else:
            cache = []
            for key, value in _dict.items(): cache.append(value)
            return cache[0][0] == cache[1][1] and cache[0][1] == cache[1][0]
