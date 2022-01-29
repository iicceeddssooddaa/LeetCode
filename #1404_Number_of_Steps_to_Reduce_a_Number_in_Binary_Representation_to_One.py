class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        if int(s[1:]) == False:
            return len(s) - 1
        count = 0
        #char_list = []
        #char_list[:] = s
        i = len(s) - 1
        while s[i] == "0":
            i -= 1
            count += 1
        counter = collections.Counter(s[:i + 1])
        return len(s[:i + 1]) + counter['0'] + 1 + count
