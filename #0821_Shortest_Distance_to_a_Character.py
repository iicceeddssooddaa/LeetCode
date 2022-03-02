class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        pos, sto, j = [], [], 0
        for i in range(len(s)):
            if s[i] == c: pos.append(i)
        for i in range(len(s)):
            if i <= pos[0]: sto.append(pos[0] - i)
            elif i >= pos[-1]: sto.append(i - pos[-1])
            elif i < pos[j + 1]: sto.append(min(i - pos[j], pos[j + 1] - i))
            elif i == pos[j + 1]:
                    j += 1
                    sto.append(0)
        return sto
