class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.stack = []
        self.stack[:] = re.split('(\d+)', compressedString)
        del self.stack[-1]
        self.pointer = 1

    def next(self):
        """
        :rtype: str
        """
        while self.pointer < len(self.stack):
            if int(self.stack[self.pointer]) > 0:
                self.stack[self.pointer] = int(self.stack[self.pointer]) - 1
                return self.stack[self.pointer - 1]
            else: self.pointer += 2
        return " "
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer < len(self.stack):
            if self.stack[self.pointer] > 0: return True
            else: self.pointer += 2
        return False if self.pointer > len(self.stack) else True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
