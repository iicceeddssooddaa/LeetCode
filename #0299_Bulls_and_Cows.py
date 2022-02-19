class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n, a, b, count1, count2 = len(secret), 0, 0, collections.Counter(secret), collections.Counter(guess)
        a = sum(secret[i] == guess[i] for i in range(n))
        for key, value in count2.items():
            if key not in count1: pass
            else: b += min(value, count1[key])
        b -= a
        return str(a) + "A" + str(b) + "B"
