class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        word_list = []
        for word in words:
            if word[0] in set1:
                i = 0
                while word[i] in set1 and i < len(word) - 1:
                    i += 1
                if i == len(word) - 1 and word[i] in set1:
                    word_list.append(word)
            if word[0] in set2:
                i = 0
                while word[i] in set2 and i < len(word) - 1:
                    i += 1
                if i == len(word) - 1 and word[i] in set2:
                    word_list.append(word)
            if word[0] in set3:
                i = 0
                while word[i] in set3 and i < len(word) - 1:
                    i += 1
                if i == len(word) - 1 and word[i] in set3:
                    word_list.append(word)
        return word_list
