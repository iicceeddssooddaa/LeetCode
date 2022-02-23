class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1, stack2 = [], []
        for i in range(len(s)):
            if s[i] == "#" and len(stack1) == 0: continue
            elif s[i] != "#": stack1.append(s[i])
            else: stack1.pop()
        for i in range(len(t)):
            if t[i] == "#" and len(stack2) == 0: continue
            elif t[i] != "#": stack2.append(t[i])
            else: stack2.pop()
        if len(stack1) != len(stack2): return False
        for i in range(len(stack1)):
            if stack1[i] != stack2[i]: return False
        return True
