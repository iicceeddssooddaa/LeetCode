class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack, n = [], len(ops)
        for i in range(n):
            if ops[i] == "C": stack.pop()
            elif ops[i] == "D": stack.append(stack[-1] *2)
            elif ops[i] == "+": stack.append(stack[-2] + stack[-1])
            else: stack.append(int(ops[i]))
        return sum(stack)
