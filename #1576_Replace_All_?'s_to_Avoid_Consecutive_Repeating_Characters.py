class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, i = [], 1
        if s[0] == "?":
            if len(s) == 1: return "a"
            elif s[1] == "a": stack.append("b")
            else: stack.append("a")
        else: stack.append(s[0])
        while i < len(s):
            if s[i] != "?": 
                stack.append(s[i])
                i += 1
            else:
                if i == len(s) - 1:
                    if stack[-1] == "a": stack.append("b")
                    else: stack.append("a")
                else:
                    if stack[-1] != "a" and s[i + 1] != "a": stack.append("a")
                    elif set([stack[-1], s[i + 1]]) == {"a", "b"}: stack.append("c")
                    else: stack.append("b")
                i += 1
        string = "".join(stack)
        return string
