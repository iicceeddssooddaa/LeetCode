class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        _list = time.split(":")
        hour, minute = _list[0], _list[1]
        if "?" in hour:
            if hour == "??": cache1 = 23
            elif hour[0] == "?":
                if int(hour[1]) < 4: cache1 = 20 + int(hour[1])
                else: cache1 = 10 + int(hour[1])
            else:
                if int(hour[0]) == 2: cache1 = 23
                else: cache1 = 10*int(hour[0]) + 9
        else: cache1 = int(hour)
        if "?" in minute:
            if minute[1] == "?": cache2 = 9
            else: cache2 = int(minute[1])
            if minute[0] == "?": cache2 += 50
            else: cache2 += 10 * int(minute[0])
        else: cache2 = int(minute)
        string = format(cache1, '02d') + ":" + format(cache2, '02d')
        return string
--------
# 查字典！
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        _list = time.split(":")
        hour, minute = _list[0], _list[1]
        
        hour_dict = {"??": "23", "0?":"09", "1?":"19", "2?": "23", "?0": "20", "?1": "21", "?2": "22", "?3": "23", "?4": "14", "?5": "15", "?6": "16", "?7": "17", "?8": "18", "?9": "19"}
        minute_dict = {"??": "59", "0?":"09", "1?": "19", "2?": "29","3?":"39", "4?": "49", "5?": "59", "?0": "50", "?1": "51", "?2": "52", "?3": "53", "?4": "54", "?5": "55", "?6": "56", "?7": "57", "?8": "58", "?9": "59"}
        
        if "?" in hour: hour = hour_dict[hour]
        if "?" in minute: minute = minute_dict[minute]
        string = hour + ":" + minute
        return string
