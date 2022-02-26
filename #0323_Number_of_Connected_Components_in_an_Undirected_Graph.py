class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if len(edges) == 0: return n
        traversed, next_v, cc_count, neighbors = set(), 0, 0, {}
        
        for edge in edges:
            if edge[0] not in neighbors: neighbors[edge[0]] = set([edge[1]])
            else: neighbors[edge[0]].add(edge[1])
            if edge[1] not in neighbors: neighbors[edge[1]] = set([edge[0]])
            else: neighbors[edge[1]].add(edge[0])
                    
        while len(traversed) != n:
            cc_count += 1
            reachable, visited = deque([next_v]), set()
            if next_v not in neighbors: 
                traversed.add(next_v)
                while next_v < n and next_v in traversed: next_v += 1
                continue
            while len(reachable) != 0:
                node = reachable.popleft()
                if node in visited: continue
                visited.add(node)
                for i in neighbors[node]: 
                    neighbors[i].remove(node)
                    reachable.append(i)
            traversed = traversed.union(visited)
            while next_v < n and next_v in traversed: next_v += 1
        return cc_count
