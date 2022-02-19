class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        cache = 0
        for op in operations:
            if "-" in op: cache -= 1
            if "+" in op: cache += 1
        return cache
----------
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = collections.Counter(operations)
        if "X++" not in count: count["X++"] = 0
        if "++X" not in count: count["++X"] = 0
        if "X--" not in count: count["X--"] = 0
        if "--X" not in count: count["--X"] = 0
        return count["X++"] + count["++X"] - count["X--"] - count["--X"]
