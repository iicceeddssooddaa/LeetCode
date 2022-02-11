class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n %3 != 0:
            return False
        stack = []
        for i in range(n):
            if s[i] == "a": stack.append("a")
            elif s[i] == "b" and len(stack) == 0: return False
            elif s[i] == "b": stack.append("b")
            elif s[i] == "c" and len(stack) < 2: return False
            elif s[i] == "c" and stack[-2] == "a" and stack[-1] == "b": del stack[-2:]
            else: return False
        return len(stack) == 0
