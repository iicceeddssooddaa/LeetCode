class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sto = []
        sto[:] = s.lower()
        cache, result = [], []
        for i in range(len(sto)):
             if sto[i] > "9": cache.append([i, sto[i], sto[i].upper()])
        n = len(cache)
        for i in range(2 ** n):
            x = bin(i)[2:].zfill(n)
            string = deepcopy(sto)
            result.append(string)
            for j in range(n):
                result[-1][cache[j][0]] = cache[j][int(x[j]) + 1]
            string = "".join(result[-1])
            result[-1] = string
        return result
