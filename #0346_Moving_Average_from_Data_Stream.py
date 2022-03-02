class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.queue = deque([])
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size: self.queue.popleft()
        self.queue.append(val)
        return sum(self.queue)/float(len(self.queue))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
