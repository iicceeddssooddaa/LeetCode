class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        sto = [first]
        for code in encoded: 
            sto.append(sto[-1] ^ code)
        return sto
