class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        n = len(s)
        for i in range(n):
            if len(stack) == 0: stack.append([s[i],1])
            elif s[i] == stack[-1][0]:
                if stack[-1][1] == k - 1: del stack[-1]
                else: stack[-1][1] += 1
            else: stack.append([s[i],1])
        char_list = []
        for i in range(len(stack)):
            char_list.extend(stack[i][0] * stack[i][1])
        string = "".join(char_list)
        return string
