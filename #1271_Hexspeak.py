class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        x = hex(int(num)).lstrip("0x")
        if "2" in x or "3" in x or "4" in x or "5" in x or "6" in x or "7" in x or "8" in x or "9" in x: return "ERROR"
        x1 = x.replace("0", "O").replace("1","I").upper()
        return x1
