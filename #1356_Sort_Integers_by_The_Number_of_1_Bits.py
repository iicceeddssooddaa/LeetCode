class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def countBits(n):
            count = 0
            while n > 0:
                count += n%2
                n //= 2
            return count
        
        sto = []
        for num in arr: sto.append([countBits(num), num])
        sto.sort()
        result = [sto[i][1] for i in range(len(sto))]
        return result
