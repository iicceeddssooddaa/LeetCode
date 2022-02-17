class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 1: return min(costs[0][0], costs[0][1], costs[0][2])
        r, g, b = [], [], []
        r.append(costs[1][0] + min(costs[0][1], costs[0][2]))
        g.append(costs[1][1] + min(costs[0][2], costs[0][0]))
        b.append(costs[1][2] + min(costs[0][0], costs[0][1]))
        
        r.append(costs[0][0])
        g.append(costs[0][1])
        b.append(costs[0][2])
        
        if n == 2: return min(r[0], g[0], b[0])
        for i in range(2,n + 1):
            r[i%2], g[i%2], b[i%2] = costs[i - 1][0] + min(g[(i - 1)%2], b[(i - 1)%2]), costs[i - 1][1] + min(b[(i - 1)%2], r[(i - 1)%2]), costs[i - 1][2] + min(g[(i - 1)%2], r[(i - 1)%2])
        return min(r[n%2], g[n%2], b[n%2])
