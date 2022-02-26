class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination: return True
        reachable, visited, neighbors = deque([source]), set(), {}
        for edge in edges:
            if edge[0] not in neighbors: neighbors[edge[0]] = set([edge[1]])
            else: neighbors[edge[0]].add(edge[1])
            if edge[1] not in neighbors: neighbors[edge[1]] = set([edge[0]])
            else: neighbors[edge[1]].add(edge[0])
        while len(reachable) != 0:
            node = reachable.popleft()
            visited.add(node)
            for i in neighbors[node]: 
                neighbors[i].remove(node)
                if i not in reachable: reachable.append(i)
        return destination in visited
        
---------------
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination: return True
        reachable, visited, neighbors = deque([source]), set(), {}
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
                # if i not in reachable: reachable.append(i)
                reachable.append(i)
        return destination in visited
