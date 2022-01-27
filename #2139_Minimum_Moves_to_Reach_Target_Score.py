class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        #double都用在最后啊，增量大
        #因而判断target的二进制表达长度，和maxDoubles比较。如果后者小，则都用掉，反之则target中每次乘二都翻倍。
        #剩下的，凡是后若干位中的1，都单独靠加。前面如果不足以翻倍，就一直加到目标。完
        bin_target = "{0:b}".format(target)
        enough = len(bin_target) - 1 <= maxDoubles
        if enough:
            steps = 0
            for char in bin_target[1:]:
                steps += int(char) + 1
            return steps
        steps = (target >> maxDoubles) - 1
        for char in bin_target[len(bin_target) - maxDoubles:]:
            steps += int(char) + 1
        return steps
