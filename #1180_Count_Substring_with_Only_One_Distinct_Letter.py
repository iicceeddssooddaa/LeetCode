class Solution(object):
    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1: return 1
        char, count, result = s[0], 0, 0
        for i in s:
            if char == i: count += 1
            else:
                result += count * (count + 1) // 2
                count = 1
                char = i
        result += count * (count + 1) // 2
        return result
