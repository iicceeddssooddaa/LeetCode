class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        n = len(accounts)
        wealthy = 0
        for account in accounts:
            wealthy = max(sum(account), wealthy)
        return wealthy
