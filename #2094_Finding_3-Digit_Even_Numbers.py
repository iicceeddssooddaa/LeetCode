class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        _dict, result = collections.Counter(digits), []
        for i in range(100,1000,2):
            a, b, c = i//100, (i%100)//10, i%10
            if (a not in _dict) or (b not in _dict) or (c not in _dict): continue
            cache = collections.Counter([a,b,c])
            can_record = True
            for key, value in cache.items():
                if _dict[key] < value: can_record = False
            if can_record: result.append(i)
        return result
