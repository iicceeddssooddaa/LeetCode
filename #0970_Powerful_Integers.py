class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound < 2:
            return []
        powerx, powery, i, j, result, result_list = {}, {}, 0, 0, {2}, []
        # 造字典
        if x == 1:
            powerx[0] = 1
        else:
            while x ** i < bound:
                powerx[i] = x ** i
                i += 1
        if y == 1:
            powery[0] = 1
        else:
            while y ** j < bound:
                powery[j] = y ** j
                j += 1
        for exp1, pow1 in powerx.items():
            for exp2, pow2 in powery.items():
                if pow1 + pow2 <= bound:
                    result.add(pow1 + pow2)
        result_list = list(result)
        return result_list
        # 思考：1.是否需要遍历两个dict？2.是否需要两个dict？
