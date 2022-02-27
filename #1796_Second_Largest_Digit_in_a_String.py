class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        _dict, count = collections.Counter(s), 0
        for i in range(9,-1,-1):
            if str(i) in _dict: count += 1
            if count == 2: return i
        return -1
