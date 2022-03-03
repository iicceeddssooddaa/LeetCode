class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(arr1)
        sto, cache = [], []
        # for i in range(len(arr2)):
        #     _dict[i] = arr2[i]
        for num in arr1:
            if num not in arr2: sto.append(num)
        sto.sort()
        for i in range(len(arr2)):
            cache.extend([arr2[i]]*counter[arr2[i]])
        cache.extend(sto)
        return cache
