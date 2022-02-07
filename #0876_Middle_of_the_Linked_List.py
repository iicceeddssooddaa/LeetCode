# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        cur = head
        mid = head
        while cur:
            if count ^ 0:
                mid = mid.next
            count ^= 1
            cur = cur.next
        return mid
