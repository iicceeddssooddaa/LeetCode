class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] < i:
                i += 1
            elif arr[i] == i:
                return i
            else:
                break
        return -1
---------------
class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] < mid:
                left = mid + 1
            elif arr[mid] > mid:
                right = mid - 1
        if arr[left] == left:
            return left
        else:
            return -1
        # 问题：可能存在多个，需要返回最小。因而恐怕需要考虑迭代。
------------
# 解决方案：扩充边界条件，对于空列返回-1。凡是遇到相等，对前面序列跑迭代程序。返回较小的可能值。这样仅对存在的做反复检查。没有重合的不会进入迭代。
class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 0:
            return -1
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                result = self.fixedPoint(arr[0:mid])
                return mid if result == -1 else result
            elif arr[mid] < mid:
                left = mid + 1
            elif arr[mid] > mid:
                right = mid - 1
        if arr[left] == left:
            result = self.fixedPoint(arr[0:left])
            return left if result == -1 else result
        else:
            return -1
