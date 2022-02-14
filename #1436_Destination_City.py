class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        # 判断唯一一个只出现在结尾而不出现在头部的城市
        city_dict = {}
        for path in paths:
            city_dict[path[0]] = 1
            if path[1] not in city_dict: city_dict[path[1]] = -1
        for key, value in city_dict.items():
            if value == -1: return key
