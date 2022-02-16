class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth, max_depth, n = 0, 0, len(s)
        for char in s:
            if char == "(": 
                depth += 1
                max_depth = max(max_depth, depth)
            if char == ")": depth -= 1
        return max_depth
