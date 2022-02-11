class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = collections.Counter(stones)
        res = 0
        for char in jewels:
            res += counter[char]
        return res
