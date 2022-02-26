class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def relativelyPrime(num1, num2):
            while num1 != 0: num1, num2 = num2%num1, num1
            return num2 == 1
        sto = []
        for i in range(2, n + 1):
            sto.append("1/"+str(i))
            for j in range(2, i):
                if relativelyPrime(j, i): sto.append(str(j)+"/"+str(i))
        return sto
