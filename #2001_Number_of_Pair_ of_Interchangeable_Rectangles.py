class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        _dict = {}
        for rectangle in rectangles:
            if float(rectangle[0])/float(rectangle[1]) not in _dict:
                _dict[float(rectangle[0])/float(rectangle[1])] = 1
            else:
                _dict[float(rectangle[0])/float(rectangle[1])] += 1
        count = 0
        print _dict
        for key, value in _dict.items():
            count += value * (value - 1) //2
        return count
      #标签用数论，说明还是要用最简整数比
      
