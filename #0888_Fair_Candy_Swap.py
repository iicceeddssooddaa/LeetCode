class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        diff, setb = sum(aliceSizes) - sum(bobSizes), set(bobSizes)
        for num in aliceSizes: 
            if num - diff//2 in setb: return [num, num - diff//2]
