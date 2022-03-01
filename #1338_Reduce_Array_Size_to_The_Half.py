class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count, sto, total, i = collections.Counter(arr), [], 0, 0
        for key, value in count.items(): sto.append(value)
        sto.sort(reverse = True)
        while total < len(arr)//2:
            total += sto[i]
            i += 1
        return i
