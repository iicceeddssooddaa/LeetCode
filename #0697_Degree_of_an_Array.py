class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, max_freq, max_dict = collections.Counter(nums), 0, {}
        for key, value in counter.items(): max_freq = max(max_freq, value)
        for key, value in counter.items():
            if value == max_freq: max_dict[key] = [-1]
        print max_dict
        i, j, length = 0, len(nums) - 1, len(nums)
        while i < len(nums):
            if nums[i] in max_dict and len(max_dict[nums[i]]) == 1:  max_dict[nums[i]].append(i)
            i += 1
        while j > -1:
            if nums[j] in max_dict and len(max_dict[nums[j]]) == 2: max_dict[nums[j]].append(j)
            j -= 1
        for key, value in max_dict.items(): length = min(length, value[2] - value[1] + 1)
        return length
