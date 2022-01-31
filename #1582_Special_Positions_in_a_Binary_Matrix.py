class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        dict1, dict2 = {}, {}
        for i in range(len(mat)):
            if i not in dict1:
                dict1[i] = 0
            for j in range(len(mat[0])):
                dict1[i] += mat[i][j]
                if j not in dict2:
                    dict2[j] = mat[i][j]
                else:
                    dict2[j] += mat[i][j]
        print dict1, dict2
        count = 0
        for key1,value1 in dict1.items():
            for key2,value2 in dict2.items():
                if value1 + value2 == 2 and mat[key1][key2] == 1:
                    count += 1
        return count
