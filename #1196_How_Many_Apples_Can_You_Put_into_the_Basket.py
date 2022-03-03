class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        weight.sort()
        i, temp, count = 0, 0, 1
        while temp <= 5000:
            if i == len(weight): break
            if temp + weight[i] > 5000: return i
            else: temp += weight[i]
            i += 1
        return i
