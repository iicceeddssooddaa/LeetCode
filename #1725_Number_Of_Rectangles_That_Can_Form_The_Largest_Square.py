class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        n, li = len(rectangles), []
        for rect in rectangles:
            li.append(min(rect[0], rect[1]))
        _dict = collections.Counter(li)
        k = max(li)
        return _dict[k]
        
----------------
class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        n, li, maxtemp, _dict = len(rectangles), [], 0, {}
        for rect in rectangles:
            temp = min(rect[0], rect[1])
            li.append(temp)
            maxtemp = max(maxtemp, temp)
            if temp not in _dict: _dict[temp] = 1
            else: _dict[temp] += 1
        # _dict = collections.Counter(li)
        return _dict[maxtemp]
