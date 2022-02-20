class Solution(object):
    def smallestFactorization(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10: return num
        proceed, sto, i = True, [], 9
        while proceed:
            proceed = False
            if num %i == 0:
                sto.append(i)
                proceed = True
                num //= i
            elif i > 2:
                i -= 1
                proceed = True
        if num > 1: return 0
        cache, j = sto[-1], len(sto) - 2
        while j >= 0:
            cache *= 10
            cache += sto[j]
            j -= 1
        return cache if cache < 2**31 else 0
