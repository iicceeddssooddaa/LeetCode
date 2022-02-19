class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        most, result = 0, []
        for candy in candies: most = max(most, candy)
        for candy in candies: result.append(True if candy + extraCandies >= most else False)
        return result
