class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1
      # 为啥这个速度有问题
---------
# 总之尽量少在return步骤做运算。下面这个👇🏻居然明显快。这都啥啊
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = n - 1
        return cache
