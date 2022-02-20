class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        i, m, n, self.arr, self.cur = 0, len(v1), len(v2), [], 0
        while i < m and i < n:
            self.arr.append(v1[i])
            self.arr.append(v2[i])
            i += 1
        if i < m: self.arr.extend(v1[i:])
        if i < n: self.arr.extend(v2[i:])
        

    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.arr[self.cur -1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.arr)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
