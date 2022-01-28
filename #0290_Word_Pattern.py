class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        list1, list2 = [], []
        list1[:] = pattern
        list2[:] = s.split(" ")
        if len(list1) != len(list2):
            return False
        counter1, counter2 = {}, {}
        for i in range(len(list1)):
            if list1[i] not in counter1:
                counter1[list1[i]] = list2[i]
            elif counter1[list1[i]] != list2[i]:
                return False
            if list2[i] not in counter2:
                counter2[list2[i]] = list1[i]
            elif counter2[list2[i]] != list1[i]:
                return False
        return True
      #由于限制双射，一本字典只能保证是映射。但存储并不大
