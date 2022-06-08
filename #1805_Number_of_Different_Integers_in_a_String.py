class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        split1 = re.findall('(\d+)', word)
        split2 = set()
        for ele in split1:
            split2.add(int(ele))
        return len(split2)
