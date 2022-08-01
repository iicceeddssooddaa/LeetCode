class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        target, time, n = tickets[k], 0, len(tickets)
        for i in range(k + 1): time += min(target, tickets[i])
        for i in range(k + 1, n): time += min(target - 1, tickets[i])
        return time
