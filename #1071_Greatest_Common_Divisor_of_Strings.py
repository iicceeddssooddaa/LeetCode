class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
        if m == n:
            if str1 == str2: return str1
            else: return ""
        
        def gcd(m,n):
            if m < n: m,n = n,m
            while n !=0: m,n = n, m%n
            return m
        
        k = gcd(m,n)
        test = str1[:k]
        for i in range(m//k):
            if str1[(i*k):((i + 1)*k)] != test: return ""
        for i in range(n//k):
            if str2[(i*k):((i + 1)*k)] != test: return ""
        return test
