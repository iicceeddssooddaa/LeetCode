class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        if target == reader.get(left): return left
        if target == reader.get(right): return right
        if target < reader.get(left) or reader.get(left) < target < reader.get(right): return -1
        cache = reader.get(right)
        while target > cache:
            left, right = right, 2 * right
            cache = reader.get(right)
            if target > cache: continue
            else:
                if target == cache: return right
                while left < right:
                    mid = (left + right) //2
                    cache = reader.get(mid)
                    if target == cache: return mid
                    elif target < cache: right = mid
                    else: left = mid
                    if left + 1 == right: break
        if target == reader.get(left): return left
        if target == reader.get(right): return right
        return -1
