class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        if ("B" not in rings) or ("G" not in rings) or ("R" not in rings): return 0
        _dict = {}
        n = len(rings)
        for i in range(0,n,2):
            if rings[i + 1] not in _dict: _dict[rings[i + 1]] = set(rings[i])
            else: _dict[rings[i + 1]].add(rings[i])
        count = 0
        for key, value in _dict.items():
            if len(value) == 3: count += 1
        return count
