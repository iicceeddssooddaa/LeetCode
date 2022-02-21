class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(p,q):
            if p < q: p, q = q, p
            while q != 0: p, q = q, p%q
            return p
        
        m, n = p//gcd(p,q), q//gcd(p,q)
        if m %2 != 0: return 0 if n %2 == 0 else 1
        return 2
