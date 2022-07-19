class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        candyset = set(candyType)
        return min(len(candyset), len(candyType)//2)
