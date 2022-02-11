class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, n = [s[0]], len(s)
        for i in range(1,n):
            if len(res) == 0: res.append(s[i])
            elif s[i] == res[-1]: res.pop()
            else: res.append(s[i])
        string = "".join(res)
        return string
