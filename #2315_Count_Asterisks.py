class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        check, count = True, 0
        for char in s:
            if char == '|': check = not check
            if check and char == '*': count += 1
        return count
