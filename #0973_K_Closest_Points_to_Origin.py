class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        _dict, dist, result = {}, [], []
        for point in points:
            cache = point[0]**2 + point[1]**2
            dist.append(cache)
            if cache not in _dict: _dict[cache] = [point]
            else: _dict[cache].append(point)
        heap1 = heapq.nsmallest(k, dist)
        for ele in heap1:
            if len(result) < k: result.extend(_dict[ele])
            else: break
        return result
