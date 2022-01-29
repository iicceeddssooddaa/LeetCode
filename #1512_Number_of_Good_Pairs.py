class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_dict = {}
        for pos,num in enumerate(nums):
            if num not in pos_dict:
                pos_dict[num] = [pos]
            else:
                pos_dict[num].append(pos)
        count = 0
        for key, _list in pos_dict.items():
            count += len(_list) * (len(_list) - 1) // 2
        return count
