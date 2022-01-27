class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        #0:z, 2:w, 8:g, 6:x, 7:s, 5:v, 4:f, 3:h, 1:o, 9:i
        counter = collections.Counter(s)
        count_0, count_2, count_4, count_6, count_8 = counter['z'], counter['w'], counter['u'], counter['x'], counter['g']
        counter['o'] -= count_0 + count_2 + count_4
        count_1 = counter['o']
        counter['h'] -= count_8
        count_3 = counter['h']
        counter['s'] -= count_6
        count_7 = counter['s']
        counter['v'] -= count_7
        count_5 = counter['v']
        counter['i'] -= count_5 + count_6 + count_8
        count_9 = counter['i']
        _str = "0"*count_0 + "1"*count_1 +"2"*count_2 + "3"*count_3 + "4"*count_4 + "5"*count_5 + "6"*count_6 + "7"*count_7 + "8"*count_8 + "9"*count_9
        return _str
        
