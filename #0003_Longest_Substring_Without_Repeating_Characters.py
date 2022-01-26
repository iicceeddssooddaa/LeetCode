class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        Dict = {s[0]:0}
        DP = [1]
        for i in range(1, len(s)):
            if s[i] not in Dict:
                DP.append(DP[i - 1] + 1)
            else:
                DP.append(min(DP[i - 1] + 1, i - Dict[s[i]]))
            Dict[s[i]] = i
        return max(DP)
