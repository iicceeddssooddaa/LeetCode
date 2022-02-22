class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        
        def threeXplus1(num):
            count = 0
            while num > 1:
                if num%2 == 0:
                    num //=2
                    count += 1
                else:
                    num *= 3
                    num += 1
                    count += 1
            return count
        
        sto = []
        for i in range(lo, hi + 1): sto.append([threeXplus1(i), i])
        sto.sort()
        return sto[k - 1][1]
