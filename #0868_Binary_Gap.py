class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = "{0:b}".format(n)
        k, max_dist, i, j = len(string), 0, 0, 1
        while i < j < k:
            if string[j] == "1":
                max_dist = max(max_dist, j - i)
                i = j
                j += 1
            else: j += 1
        return max_dist
