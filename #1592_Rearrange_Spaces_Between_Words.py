class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        space = text.count(" ")
        word_list = [item for item in text.split(" ") if item]
        n = len(word_list) - 1
        if n == 0:
            word_list.append(" "*space)
            result = "".join(word_list)
            return result
        interval = space // n
        rem = space % n
        if rem != 0:
            str_rem = " "*rem
            word_list.append(str_rem)
        for i in range(n):
            word_list.insert((2*i + 1), " "*interval)
        result = "".join(word_list)
        return result
