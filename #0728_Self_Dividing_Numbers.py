class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def isDividingNumber(num):
            string = str(num)
            if "0" in string: return False
            for digit in string:
                if num % int(digit) != 0 : return False
            return True
            
        sto = []
        for num in range(left, right + 1):
            if isDividingNumber(num): sto.append(num)
        return sto
