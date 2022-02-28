class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.queue = [i for i in range(1,n + 1)]

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        self.queue.append(self.queue[k - 1])
        del self.queue[k - 1]
        return self.queue[-1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

----------
class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.dict, self.pointer = OrderedDict(), n
        for i in range(1,n + 1):
            self.dict[i] = 1

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        key, cache = self.dict.items()[k - 1]
        self.dict.pop(key)
        self.dict[key] = 1
        return key
    

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
