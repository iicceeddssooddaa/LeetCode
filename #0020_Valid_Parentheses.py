class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sto, i = [], 0
        if len(s) %2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in {"(", "[", "{"}:
                sto.append(s[i])
            if s[i] in {")", "]", "}"}:
                if len(sto) == 0: return False
                elif s[i] == ")" and sto[-1] == "(":
                    sto.pop()
                elif s[i] == "]" and sto[-1] == "[":
                    sto.pop()
                elif s[i] == "}" and sto[-1] == "{":
                    sto.pop()
                else:
                    return False
        if len(sto) != 0:
            return False
        return True
