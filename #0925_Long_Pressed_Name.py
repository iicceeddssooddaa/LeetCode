class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name[0] != typed[0] or name[-1] != typed[-1]: return False
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if name[i - 1] == typed[j]: j += 1
                else: return False
        while i == len(name) and j < len(typed) and name[-1] == typed[j]: j += 1        
        return (i == len(name)) and (j == len(typed))
