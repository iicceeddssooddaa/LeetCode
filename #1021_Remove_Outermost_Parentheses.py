class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, n = [], len(s)
        # 用指针计数比序列增删容易，底层的时间复杂度低
        left, right = 0, 0
        for i in range(n):
            if s[i] == "(": left += 1
            if s[i] == ")": right += 1
              # 如遇相同则表示首尾，清零即可
            if left == right:
                left = 0
                right = 0
              # 1，0表示首个左括号，不做动作
            elif left == 1 and right == 0:
                continue
              # 余下存储
            else: res.append(s[i])
        string = "".join(res)
        return string
