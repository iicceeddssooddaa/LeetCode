class RecentCounter(object):

    def __init__(self):
        self.sto = deque([])

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.sto.append(t)
        while self.sto[0] < t - 3000: self.sto.popleft()
        return len(self.sto)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
