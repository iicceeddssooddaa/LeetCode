class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start, end = rounds[0], rounds[-1]
        if start <= end: result = [i for i in range(start, end + 1)]
        else: 
            result = [i for i in range(1, end + 1)]
            result1 = [i for i in range(start, n + 1)]
            result.extend(result1)
        return result
