class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0,1,1]
        for i in range(3,n + 1):
            T.append(T[i - 3] + T[i - 2] + T[i - 1])
        return T[n]
        #可以考虑直接模运算迭代，只用四位
-------
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0,1,1]
        for i in range(3,n + 1): T[i%3] = T[(i - 3)%3] + T[(i - 2)%3] + T[(i - 1)%3]
        return T[n%3]
