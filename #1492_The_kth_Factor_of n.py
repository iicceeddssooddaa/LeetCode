class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #i计因子，count计因子个数
        i, count = 2, 1
        while i <= n and count < k:
            count += 1 if n%i == 0 else 0
            i += 1
        return i-1 if count == k else -1
        #速度有问题？这个遍历不是挺直接了么。
        #哦对，可以成对计。造表。如果到了平方根还没到计数一半，返回-1，否则i未到平方根直接返回，或者超过了算对偶然后查表。
