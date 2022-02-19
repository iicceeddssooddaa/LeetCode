class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter, sto, result = collections.Counter(s), [], []
        for key, value in counter.items(): sto.append([-1 * value,key])
        sto.sort()
        for record in sto: result.extend([record[1]] * (-1 * record[0]))
        string = "".join(result)
        return string
