class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        n, tax, cache = len(brackets), 0, 0
        for i in range(n):
            diff = brackets[i][0] - cache
            tax += brackets[i][1] * min(income, diff)
            if income <= diff: break
            else: income -= diff
            cache = brackets[i][0]
        return float(tax)/100
