class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        sto, temp = [], float('inf')
        for i in range(len(timePoints)): sto.append(int(timePoints[i][0:2])*60 + int(timePoints[i][3:5]))
        sto.sort()
        sto.append(sto[0] + 1440)
        for i in range(len(timePoints)): temp = min(sto[i + 1] - sto[i], temp)
        return temp
