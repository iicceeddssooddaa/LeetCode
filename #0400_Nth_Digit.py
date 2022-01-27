class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        last_count = 0
        new_count = 9
        #last_count < n <= new_count 来锁定位数
        i = 2
        while new_count < n:
            last_count = new_count
            new_count += i * 9 * 10**(i - 1)
            i += 1
        t = i - 1 
        #number of digits
        full_length = (n - last_count - 1)//t 
        # it is the full_length +1 st number of length t, or full_length th number from 10**(t - 1)
        pos = (n - last_count)%t if (n - last_count)%t !=0 else t
        # the pos th digit, if 0 then the last
        target_num = 10**(t - 1) + full_length
        return str(target_num)[pos - 1]
