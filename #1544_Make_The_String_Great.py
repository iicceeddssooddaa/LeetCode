class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, n = [], len(s)
        for i in range(n):
            if len(stack) == 0: stack.append(s[i])
            elif (s[i].islower() and s[i].upper() == stack[-1])or (s[i].isupper() and s[i].lower() == stack[-1]): del stack[-1]
            else: stack.append(s[i])
        string = "".join(stack)
        return string
