class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n, max_sal, min_sal, total = len(salary), float("-inf"), float("inf"), 0
        for money in salary:
            total += money
            max_sal = max(max_sal, money)
            min_sal = min(min_sal, money)
        total -= max_sal + min_sal
        return float(total)/float(n - 2)
