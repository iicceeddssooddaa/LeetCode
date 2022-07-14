class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        result, x, temp = [], 1, customfunction.f(1,1)
        while temp < z:
            x *= 2
            temp = customfunction.f(x,1)
        x_max = x if temp == z else x - 1
        y, temp = 1, customfunction.f(1,1)
        while temp < z:
            y *= 2
            temp = customfunction.f(1,y)
        right = y if temp == z else y - 1
        for x in range(1, x_max + 1):
            left = 1
            if customfunction.f(x,left) == z:
                result.append([x,left])
                continue
            elif customfunction.f(x,right) == z:
                result.append([x,right])
                continue
            else:
                while left < right:
                    mid = (left + right)//2
                    temp = customfunction.f(x,mid)
                    if temp == z: left, right = mid, mid
                    elif temp < z: left = mid + 1
                    else: right = mid - 1
                if customfunction.f(x,left) == z: result.append([x,left])
        return result
