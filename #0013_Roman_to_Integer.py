
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        Dict1 = {'CM': 100, 'CD': 100, 'XC': 10, 'XL': 10, 'IX': 1, 'IV' : 1}
        for i,v in Dict1.items():
            if(s.find(i) != -1):
                num -= 2*v
        Dict2 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i,v in Dict2.items():
            Count = s.count(i)
            if(Count > 0):
                num += v * Count
        return num
----------------
#List处置？
#String源对象不可修改。至多生成新的。
