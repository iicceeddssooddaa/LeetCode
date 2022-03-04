class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count1, freq, count2, result = collections.Counter(words), [], {}, []
        for key, value in count1.items():
            if value not in count2: 
                count2[value] = [key]
                freq.append(value)
            else: count2[value].append(key)
        sto, i = nlargest(k, freq), 0
        while len(result) < k:
            j = 0
            count2[sto[i]].sort()
            while len(result) < k and j < len(count2[sto[i]]):
                result.append(count2[sto[i]][j])
                j += 1
            i += 1
        return result
