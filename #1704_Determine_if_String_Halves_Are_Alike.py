class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s) // 2
        count1, count2 = sum(s[i] in vowel for i in range(0,n)), sum(s[i] in vowel for i in range(n,2*n))
        return count1 == count2
