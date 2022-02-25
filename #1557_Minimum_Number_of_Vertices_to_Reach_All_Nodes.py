class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        head, tail = set(), set()
        for edge in edges:
            if edge[0] not in tail: head.add(edge[0])
            tail.add(edge[1])
            if edge[1] in head: head.remove(edge[1])
        for i in range(n):
            if i not in head and i not in tail: head.add(i)
        return list(head)
