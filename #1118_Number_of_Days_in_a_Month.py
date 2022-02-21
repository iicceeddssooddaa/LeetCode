class Solution(object):
    def numberOfDays(self, year, month):
        """
        :type year: int
        :type month: int
        :rtype: int
        """
        month_dict = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if month in month_dict: return month_dict[month]
        if year % 4 != 0: return 28
        if year %100 == 0 and year % 400 != 0: return 28
        return 29
