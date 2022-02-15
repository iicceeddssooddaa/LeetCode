class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # 参考Two sum修字典的方式。构造二倍和一半（若偶数）的集合，检查存在性。不存在则加词条。
        # 遍历复杂度O(n)，查集合的强度需要回顾O(1)。因而等价于遍历复杂度。考虑到无法近似而跳跃，避开排序不太有显著下降
        cache = set()
        for num in arr:
            if num in cache: return True
            else: 
                cache.add(num * 2)
                if not num & 1: cache.add(num //2)
        return False
