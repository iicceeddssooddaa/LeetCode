class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        sto, _dict, result = set(), {}, []
        for key, value in counter.items():
            sto.add(value)
            if value not in _dict:
                _dict[value] = [key]
            else: _dict[value].append(key)
        ref = sorted(sto)
        for i in ref:
            if len(_dict[i]) == 1: result.extend([_dict[i][0]] * i)
            else: 
                _dict[i].sort(reverse = True)
                for num in _dict[i]: result.extend([num] * i)
        return result
