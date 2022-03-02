class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, left, right, pointer = 0, 0, 0, 0
        while pointer < len(s):
            if s[pointer] == "L": left += 1
            elif s[pointer] == "R": right += 1
            if left == right and left != 0:
                count += 1
                left = 0
                right = 0
            pointer += 1
        return count
