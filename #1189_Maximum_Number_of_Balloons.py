class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = {"a":0, "b":0, "n":0, "l":0, "o":0}
        for char in text:
            if char not in counter: counter[char] = 1
            else: counter[char] += 1        
        return min(counter["b"], counter["a"], counter["n"], counter["l"]//2, counter["o"]//2)
