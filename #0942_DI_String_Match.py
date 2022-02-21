class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        sto, i, j, k = [], 0, len(s), 0
        while k < len(s):
            if s[k] == "I": 
                sto.append(i)
                i += 1
            elif s[k] == "D":
                sto.append(j)
                j -= 1
            k += 1
        sto.append(i)
        return sto
