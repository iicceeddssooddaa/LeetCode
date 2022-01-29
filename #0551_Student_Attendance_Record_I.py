class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count, con_l_count = 0, 0
        for char in s:
            if char == "A":
                a_count += 1
                con_l_count = 0
                if a_count == 2:
                    return False
            if char == "L":
                con_l_count += 1
                if con_l_count >= 3:
                    return False
            if char == "P":
                con_l_count = 0
        return True
