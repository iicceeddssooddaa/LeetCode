class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        id_list, score, j = set(), [], 0
        for record in items:
            record[1] *= -1
            id_list.add(record[0])
        items.sort()
        for i in id_list:
            while items[j][0] != i: j += 1
            high_five = (items[j][1] + items[j + 1][1] + items[j + 2][1] + items[j + 3][1] + items[j + 4][1]) * (-1)
            score.append([i, high_five //5])
        return score
