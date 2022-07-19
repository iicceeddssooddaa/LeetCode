class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start == destination: return 0
        end1, end2, route1, route2, i = min(start, destination), max(start, destination), 0, 0, 0
        for i in range(end1):
            route1 += distance[i]
        for i in range(end1, end2):
            route2 += distance[i]
        for i in range(end2, len(distance)):
            route1 += distance[i]
        return min(route1, route2)
