class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        _dict = {}
        index = {}
        for pos, item in enumerate(list1):
             _dict[item] = -pos
        for pos, item in enumerate(list2):
            if item in _dict:
                pos_sum = _dict[item]*(-1) + pos
                if pos_sum not in index:
                    index[pos_sum] = [item]
                else:
                    index[pos_sum].append(item)
        min_sum = min(key for key in index)
        return index[min_sum]
