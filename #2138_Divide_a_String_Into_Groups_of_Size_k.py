class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if len(s)%k != 0:
            t = (-len(s)) % k
            s = s + fill*t
        sto = [s[k *i: k *(i + 1)] for i in range(len(s)//k)]
        return sto
