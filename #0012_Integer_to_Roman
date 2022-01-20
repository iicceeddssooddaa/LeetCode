class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Dict0 = {0:1000, 1:900, 2:500, 3:400, 4:100, 5:90, 6:50, 7:40, 8:10, 9:9, 10:5, 11:4, 12:1}
        Dict2 = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        List = []
        for i in range(13):
            count = num//Dict0[i]
            num %= Dict0[i]
            if count != 0:
                List.append(Dict2[Dict0[i]]*count)
        String = "".join(List)
        return String
