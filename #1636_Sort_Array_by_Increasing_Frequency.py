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
----------
# 既然能用上高维列表的排序，当然要用。如果同频则降序，那么构造[频次,-1 * 数字]的序列进行排序即可。然后还原。
# 快多了。
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        sto, result = [], []
        for key, value in counter.items(): sto.append([value, -1 * key])
        sto.sort()
        for record in sto: result.extend([record[1]*-1] * record[0])
        return result
