class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count5, count10 = 0, 0
        for bill in bills:
            if bill == 5: count5 += 1
            if bill == 10:
                if count5 > 0: 
                    count5 -= 1
                    count10 += 1
                else: return False
            if bill == 20:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else: return False
        return True
