class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #倒序循环，如遇9，翻成0
        #留下新的i位待进位
        i = len(digits) - 1
        while i > 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        #判断此时首位（若后续都是9）是否同样是9，如是进位，如否加一
        if digits[i] == 9:
            digits[i] = 0
            digits.insert(0,1)
        else:
            digits[i] += 1
        return digits
