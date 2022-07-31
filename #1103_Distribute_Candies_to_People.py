class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        result, pos = [0] * num_people, 1
        while candies > 0:
            result[(pos - 1) %num_people] += min(candies, pos)
            candies -= pos
            pos += 1
        return result
