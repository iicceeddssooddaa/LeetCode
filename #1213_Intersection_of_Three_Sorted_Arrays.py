class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        log, result, n0, n1, n2 = [0,0], [], len(arr1), len(arr2), len(arr3)
        for i in range(n2):
            in0, in1 = False, False
            left, right = log[0], n0 - 1
            if arr3[i] > arr1[right] or left > right: break
            if arr3[i] == arr1[left]: log[0], in0 = left + 1, True
            elif arr3[i] == arr1[right]: log[0], in0 = right, True
            else:
                while left < right:
                    mid = (left + right)//2
                    if arr3[i] == arr1[mid]: log[0], in0, left = mid + 1, True, right
                    elif arr3[i] < arr1[mid]: right = mid - 1
                    else: left = mid + 1
                if arr3[i] == arr1[left]: log[0], in0 = left + 1, True
            if not in0: continue
            
            left, right = log[1], n1 - 1
            if arr3[i] > arr2[right] or left > right: break
            if arr3[i] == arr2[left]: log[1], in1 = left + 1, True
            elif arr3[i] == arr2[right]: log[1], in1 = right, True
            else:
                while left < right:
                    mid = (left + right)//2
                    if arr3[i] == arr2[mid]: log[1], in1, left = mid + 1, True, right
                    elif arr3[i] < arr2[mid]: right = mid - 1
                    else: left = mid + 1
                if arr3[i] == arr2[left]: log[1], in1 = left + 1, True
            if in1: result.append(arr3[i])
        return result
