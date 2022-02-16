class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, counter = 0, collections.Counter(nums)
        for key in counter:
            if k - key != key and k - key in counter:
                contribute = min(counter[key], counter[k - key])
                count += contribute
                counter[key] -= contribute
                counter[k - key] -= contribute
            if k - key == key:
                contribute = counter[key]//2
                count += contribute
                counter[key] -= contribute * 2
        return count
