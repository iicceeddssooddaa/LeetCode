class Vector2D(object):

    def __init__(self, vec):
        """
        :type vec: List[List[int]]
        """
        n, self.sto, self.pos = len(vec), [], 0
        for i in range(n):
            self.sto.extend(vec[i])

    def next(self):
        """
        :rtype: int
        """
        self.pos += 1
        return self.sto[self.pos - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < len(self.sto)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
