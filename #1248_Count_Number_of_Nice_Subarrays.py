class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 我们只关心实质结构[偶数的个数，一个奇数，偶数的个数，一个奇数，。。。，偶数的个数]
        # 最终结果就是连续k个奇数前后偶数的个数（分别加一）乘积之和
        # 计数问题
        count, n, parity_list = 0, len(nums), []
        for i in range(n):
            count += 1
            if nums[i] & 1:
                parity_list.append(count)
                count = 0
        count += 1
        parity_list.append(count)
        if len(parity_list) <= k:
            return 0
        total = 0
        for i in range(0, len(parity_list)-k):
            total += parity_list[i] * parity_list[i + k]
        return total
