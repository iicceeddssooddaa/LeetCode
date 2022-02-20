class HitCounter(object):

    def __init__(self):
        self.sto = deque([])

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.sto.append(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        notdone = True
        while len(self.sto) > 0 and notdone:
            if self.sto[0] <= timestamp - 300: 
                self.sto.popleft()
            else: notdone = False
        return len(self.sto)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
