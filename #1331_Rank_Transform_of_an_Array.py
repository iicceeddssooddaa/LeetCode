class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 由于需要判断顺序及排重，复杂度或许在O(nlogn)的基础上增加
        # 去重排序——题目默认应该是并列后不占位置，即并列第一后依然是第二
        # 造个字典计序，最后遍历一次改写为排位
        numset = set(arr)
        cache, _dict = [], {}
        cache[:] = numset
        cache.sort()
        for index,value in enumerate(cache):
            _dict[value] = index + 1
        for i in range(len(arr)):
            arr[i] = _dict[arr[i]]
        return arr
