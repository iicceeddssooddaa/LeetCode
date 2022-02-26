class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1: return True
        if len(edges) != n - 1: return False
        visited = set()
        for edge in edges:
            visited.add(edge[0])
            visited.add(edge[1])
        if len(visited) != n: return False
        reachable, visited, neighbors = deque([0]), set(), {}
        for edge in edges:
            if edge[0] not in neighbors: neighbors[edge[0]] = set([edge[1]])
            else: neighbors[edge[0]].add(edge[1])
            if edge[1] not in neighbors: neighbors[edge[1]] = set([edge[0]])
            else: neighbors[edge[1]].add(edge[0])
        while len(reachable) != 0:
            node = reachable.popleft()
            if node in visited: continue
            visited.add(node)
            for i in neighbors[node]: 
                neighbors[i].remove(node)
                reachable.append(i)
        return len(visited) == n
