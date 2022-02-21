class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 6: return n
        ugly = [1,2,3,4,5,6]
        point2, point3, point5 = 3, 2, 1
        while len(ugly) != n:
            if 2 * ugly[point2] < min(3 * ugly[point3], 5 * ugly[point5]): 
                ugly.append(2 * ugly[point2])
                point2 += 1
            elif 3 * ugly[point3] < min(2 * ugly[point2], 5 * ugly[point5]): 
                ugly.append(3 * ugly[point3])
                point3 += 1
            elif 5 * ugly[point5] < min(3 * ugly[point3], 2 * ugly[point2]): 
                ugly.append(5 * ugly[point5])
                point5 += 1
            elif 2 * ugly[point2] == 3 * ugly[point3] < 5 * ugly[point5]: 
                ugly.append(2 * ugly[point2])
                point2 += 1
                point3 += 1
            elif 3 * ugly[point3] == 5 * ugly[point5] < 2 * ugly[point2]: 
                ugly.append(3 * ugly[point3])
                point3 += 1
                point5 += 1
            elif 2 * ugly[point2] == 5 * ugly[point5] < 3 * ugly[point3]: 
                ugly.append(2 * ugly[point2])
                point2 += 1
                point5 += 1
            elif 2 * ugly[point2] == 3 * ugly[point3] == 5 * ugly[point5]: 
                ugly.append(2 * ugly[point2])
                point2 += 1
                point3 += 1
                point5 += 1
        return ugly[-1]
