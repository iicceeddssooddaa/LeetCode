class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if len(stack) > 1:
                if stack[-1] == stack[-2] == char: continue
                else: stack.append(char)
            else:stack.append(char)
        string = "".join(stack)
        return string
