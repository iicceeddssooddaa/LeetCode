class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        #等价于二进制下，除首位，每个1减一次，每一位挪一次。记总共n位，k个1，则操作步骤为n + k - 2
        #等价于遍历除首位全部，遇0记1，遇1记2
        if num == 0:
            return 0
        #排除首位不为1
        bin_num = "{0:b}".format(num)
        count = -1
        for char in bin_num:
            count += int(char) + 1
        return count
        #可以有更简单数1的方法？这个可以引用count 1 bits的思路。需要先改那个。
