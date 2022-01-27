class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_set = set(digits)
        #分是否长度增加
        #长度增加当且仅当全是9
        if digit_set == {9}:
            _list = [0]*len(digits)
            _list.insert(0,1)
            return _list
        #倒序指针while循环
        i = len(digits) - 1
        while i > 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        digits[i] += 1
        return digits
      #有点慢，在考虑要不直接倒序循环，最后判断要不要增加长度
