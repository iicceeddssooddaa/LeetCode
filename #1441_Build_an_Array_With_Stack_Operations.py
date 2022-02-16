class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        op = []
        for i in range(1,n + 1):
            op.append("Push")
            if i not in target: op.append("Pop")
            if i == target[-1]: break
        return op
