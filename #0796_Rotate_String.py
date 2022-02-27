class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal): return False
        if s == goal: return True
        n = len(s)
        for i in range(1, n):
            if s[0] == goal[i]:
                if s[-1 * i:] == goal[: i] and s[: -1 *i] == goal[i :]: return True
        return False
