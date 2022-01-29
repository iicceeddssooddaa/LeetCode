class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        last_single, i = True, 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                last_single = True
            else:
                i += 2
                last_single = False
        return last_single
