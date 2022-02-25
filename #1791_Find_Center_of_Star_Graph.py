class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        vertex = set(edges[0])
        return edges[1][0] if edges[1][0] in vertex else edges[1][1]
