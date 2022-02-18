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
