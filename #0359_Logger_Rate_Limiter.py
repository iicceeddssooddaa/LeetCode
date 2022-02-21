class Logger(object):

    def __init__(self):
        self.record = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.record:
            self.record[message] = timestamp
            return True
        else:
            if self.record[message] + 9 >= timestamp:
                return False
            elif self.record[message] + 10 <= timestamp:
                self.record[message] = timestamp
                return True
