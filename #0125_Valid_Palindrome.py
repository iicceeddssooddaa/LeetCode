class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string1 = s.lower()
        string2 = re.sub(r'[^a-zA-Z0-9]', '', string1)
        return string2 == string2[-1::-1]
