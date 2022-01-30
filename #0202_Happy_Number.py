class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem_set = {n}
        sum_of_squares = n
        while 1 not in mem_set:
            digit_string = str(sum_of_squares)
            digit_map = map(int, digit_string)
            digit_list = list(digit_map)
            sum_of_squares = sum(i**2 for i in digit_list)
            if sum_of_squares in mem_set:
                break
            else:
                mem_set.add(sum_of_squares)
        return 1 in mem_set
