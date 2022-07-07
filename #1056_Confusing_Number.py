class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits, test_set = str(n), set(['2','3','4','5','7']) 
        if len(test_set.intersection(set(digits))): return False
        _dict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        for i in range(len(digits)//2 + 1):
            if digits[i] != _dict[digits[-i-1]]: return True
        return False
