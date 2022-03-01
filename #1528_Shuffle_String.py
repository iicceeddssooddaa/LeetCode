class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        _dict = {}
        for i in range(len(indices)): _dict[indices[i]] = s[i]
        sto = [_dict[i] for i in range(len(indices))]
        string = "".join(sto)
        return string
