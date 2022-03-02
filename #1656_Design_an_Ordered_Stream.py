class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.list, self.ptr, self.size = ["" for _ in range(n)], 0, n

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.list[idKey - 1] = value
        self.stack = []
        while self.ptr < self.size:
            if self.list[self.ptr] != "":
                self.stack.append(self.list[self.ptr])
                self.ptr += 1
            else: break
        return self.stack


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
