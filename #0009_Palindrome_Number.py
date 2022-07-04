class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            converted_str = str(x)
            i = 0
            while (converted_str[i] == converted_str[-(i + 1)]):
                if (i == len(converted_str)//2):
                    return True
                else:
                    i+=1
            return False

---------------------
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            converted_str = str(x)
            for i in range(len(converted_str)//2):
                if (converted_str[i] != converted_str[-(i + 1)]):
                    return False
            return True
            
            #无显著提高。快过36%，少于40%
            
-------------
#核心在于翻转与判断
#判断只要一次的话，用string直接翻转。判断前后string。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            converted_str = str(x)
            reverse = converted_str[::-1]
            return (reverse==converted_str)
            #快于84%，少于90%
