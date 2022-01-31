class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list, new_word_list = [], []
        word_list[:] = s.split(" ")
        for word in word_list:
            cache, new_cache = [], []
            cache[:] = word
            new_cache = cache[::-1]
            new_word_list.append("".join(new_cache))
        return " ".join(new_word_list)
