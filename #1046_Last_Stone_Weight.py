class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        queue = []
        for i in range(len(stones)):
            heapq.heappush(queue, stones[i] * (-1))
        while len(queue) > 1: 
            temp1 = heapq.heappop(queue)
            temp2 = heapq.heappop(queue)
            if temp1 != temp2: heapq.heappush(queue, temp1 - temp2)
        return 0 if len(queue) == 0 else queue[0] * (-1)      
