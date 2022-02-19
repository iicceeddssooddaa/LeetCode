class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        _dict = {"a":1, "b":0, "c":1, "d":0, "e":1, "f":0, "g":1, "h":0}
        return (int(coordinates[1]) + _dict[coordinates[0]]) & 1
