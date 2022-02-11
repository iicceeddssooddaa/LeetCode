class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        _dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
        rec = []
        while columnNumber > 0:
            cache = columnNumber %26
            tran_cache = cache if cache != 0 else 26
            rec.insert(0,_dict[tran_cache])
            columnNumber -= tran_cache
            columnNumber //= 26
        string = "".join(rec)
        return string
