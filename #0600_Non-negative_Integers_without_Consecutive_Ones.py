class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return [1,2,3][n]
        x = "{0:b}".format(n)
        k, fib = len(x) - 1, [2,1,1]
        for i in range(4, k + 4): fib[i%3] = fib[(i - 1)%3] + fib[(i - 2)%3]
        if n * 2/3 >= 2**k: return fib[(k + 3)%3]
        else: return fib[(k + 2)%3] + self.findIntegers(n - 2**k)
-----------------------
# 有显著快一点。暴力算这时候就比反复递归强多了。
class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return [1,2,3][n]
        x = "{0:b}".format(n)
        k = len(x) - 1
        num1 = (((1 + sqrt(5))/2)**(k + 3) - ((1 - sqrt(5))/2)**(k + 3))/sqrt(5)
        num2 = (((1 + sqrt(5))/2)**(k + 2) - ((1 - sqrt(5))/2)**(k + 2))/sqrt(5)
        if n * 2/3 >= 2**k: return int(num1)
        else: return int(num2 + self.findIntegers(n - 2**k))
--------------
# 非递归版本写了一个，整体比较，还是DP最好。且由于反复递归，斐波那契数直接算快。看第二组代码。
class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        n <<= 1
        x, _list, result = "{0:b}".format(n), [], 0
        k, fib, notadd = len(x) - 2, [0,1], True
        for i in range(k + 1):
            if x[i:i + 2] == "11": 
                _list.append(k + 3 - i)
                notadd = False
                break
            elif x[i] == "1": _list.append(k + 2 - i)
        result += int(notadd)
        for i in range(2, k + 4): 
            fib[i%2] = fib[(i - 1)%2] + fib[(i - 2)%2]
            if i in _list: result += fib[i%2]
        return result
