class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack, sto, i = [], [], 0
        while i < len(command):
            if command[i] == "G": sto.append("G")
            elif command[i] == "(": stack.append("(")
            elif command[i] == ")" and stack[-1] == "(": 
                sto.append("o")
                stack.pop()
            elif command[i] == ")" and stack[-1] == "l":
                sto.append("al")
                del stack[-3:]
            else: stack.append(command[i])
            i += 1
        string = "".join(sto)
        return string
