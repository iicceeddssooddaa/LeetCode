class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            decode = [0] * len(code)
            return decode
        decode, cache, n = [], 0, len(code)
        if k > 0:
            for j in range(k):
                cache += code[(j + 1)%n]
            decode.append(cache)
            for i in range(1, len(code)):
                cache -= code[i%n]
                cache += code[(i + k)%n]
                decode.append(cache)
            return decode
        if k < 0:
            for j in range(-k):
                cache += code[(- j - 1)%n]
            decode.append(cache)
            for i in range(1, len(code)):
                cache += code[(i - 1)%n]
                cache -= code[(i + k - 1)%n]
                decode.append(cache)
            return decode
