class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # 本质在于判断 1：字符库相同，2：不计字符对应的情况下，字频相同
#         核心为置换
        n = len(word1)
#         长度不同直接pass
        if len(word2) != n: return False
#         计字频（counter），改为字频序列（freq_list），顺带字符库（set）
        counter1, counter2 = collections.Counter(word1), collections.Counter(word2)
        freq_list1, freq_list2, set1, set2 = [], [], set(), set()
        for key, value in counter1.items():
            freq_list1.append(value)
            set1.add(key)
        for key, value in counter2.items():
            freq_list2.append(value)
            set2.add(key)
#         字符库不同报错
        if set1 != set2: return False
        freq_list1.sort()
        freq_list2.sort()
        i = 0
        while i < len(freq_list1) and freq_list1[i] == freq_list2[i]:
            i += 1
#         字频排序比较
        return i == len(freq_list1)
