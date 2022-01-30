class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        dict_year = {}
        count = 0
        for i in range(1971,2101):
            if i%4 != 0:
                dict_year[i] = count
                count += 1
                count %= 7
            if i%4 == 0:
                dict_year[i] = count       
                count += 2
                count %= 7
        dict_month = {1:0, 2:3, 3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}
        day_of_week = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        is_leap_year = (year%4 ==0) and (year < 2100) and (month > 2)
        num_days = dict_year[year] + dict_month[month] + day + is_leap_year + 4
        return day_of_week[num_days%7]
