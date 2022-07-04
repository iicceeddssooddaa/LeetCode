class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        n1, n2, count = len(arr1), len(arr2), 0
        for i in range(n1):
            if arr1[i] >= arr2[-1] and arr1[i] - arr2[-1] <= d: count += 1
            elif arr1[i] <= arr2[0] and arr2[0] - arr1[i] <= d: count += 1
            else:
                left, right = 0, n2 - 1
                while left < right:
                    mid = (left + right)//2
                    if abs(arr1[i] - arr2[left]) <= d:
                        right = left
                    elif abs(arr1[i] - arr2[right]) <= d:
                        left = right
                    elif abs(arr1[i] - arr2[mid]) <= d:
                        left, right = mid, mid
                    elif arr1[i] < arr2[mid]: right = mid - 1
                    elif arr1[i] > arr2[mid]: left = mid + 1
                if abs(arr1[i] - arr2[left]) <= d and abs(arr1[i] - arr2[right]) <= d: count += 1
        return n1 - count
