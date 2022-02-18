class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        freq, sto, n = [], [], len(counter)
        for key, value in counter.items():
            freq.append([key, value])
        freq.sort()
        j, up = 0, True
        while len(sto) < len(s):
            if j == n: 
                up = False
                j = n - 1
            elif j == -1:
                up = True
                j = 0
            if up == True:
                if freq[j][1] != 0: 
                    sto.append(freq[j][0])
                    freq[j][1] -= 1
                j += 1
            elif up == False:
                if freq[j][1] != 0:
                    sto.append(freq[j][0])
                    freq[j][1] -= 1
                j -= 1
        string = "".join(sto)
        return string
