class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        pos, result = {}, [0]*len(score)
        for index, value in enumerate(score): pos[value] = index
        score.sort(reverse = True)
        for index, value in enumerate(score):
            if index == 0: result[pos[value]] = "Gold Medal"
            elif index == 1: result[pos[value]] = "Silver Medal"
            elif index == 2: result[pos[value]] = "Bronze Medal"
            else: result[pos[value]] = str(index + 1)
        return result
