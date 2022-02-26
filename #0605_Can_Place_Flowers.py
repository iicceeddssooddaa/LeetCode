class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 1: i += 2
            elif flowerbed[i] == 0 and flowerbed[i + 1] == 0: 
                n -= 1
                i += 2
            else: i += 3
            if n <= 0: return True # 貌似加上了反而速度慢
        if i == len(flowerbed) - 1 and flowerbed[-1] == 0: n -= 1
        return n <= 0
