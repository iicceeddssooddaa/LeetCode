class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True
        for index, num in enumerate(nums):
            if index + num < n and reachable[index]:
                for i in range(index, index + num + 1):
                    reachable[i] = True
            elif reachable[index]:
                for i in range(index, n):
                    reachable[i] = True
        return reachable[-1]
        # 超时
----------
# 队列先做出来了一次
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        queue = deque([0])
        while n - 1 not in queue and len(queue) != 0:
            k = nums[queue[0]]
            if len(queue) < k + 1:
                for i in range(queue[-1] + 1, queue[0] + k + 1): queue.append(i)
            queue.popleft()
        return n - 1 in queue
---------
# 也许链表可以
