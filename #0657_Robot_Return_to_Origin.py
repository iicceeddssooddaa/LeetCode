class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up, down, left, right = 0,0,0,0
        for move in moves:
            up += 1 if move == "U" else 0
            down += -1 if move == "D" else 0
            left += 1 if move == "L" else 0
            right += -1 if move == "R" else 0
        return (not (up + down)) and (not (left + right))
