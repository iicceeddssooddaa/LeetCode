class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        largest, year = 0, 1950
        for i in range(1950, 2050):
            pop = sum(record[0] <= i <record[1] for record in logs)
            if pop > largest:
                largest = pop
                year = i
        return year
