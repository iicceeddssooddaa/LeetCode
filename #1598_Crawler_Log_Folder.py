class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        level = 0
        for str in logs:
            if str == "../": level -= 1 if level > 0 else 0
            elif str == "./": continue
            else: level += 1
        return level
