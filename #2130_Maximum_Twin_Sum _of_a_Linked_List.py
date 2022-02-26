# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        sto, temp, curmax = [head.val], head, 0
        while temp.next:
            temp = temp.next
            sto.append(temp.val)
        for i in range(0, len(sto)//2): curmax = max(curmax, sto[i] + sto[-i - 1])
        return curmax
