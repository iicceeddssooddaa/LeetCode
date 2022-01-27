# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            tmp = cur.next
            while tmp and cur.val == tmp.val:
                cur.next = tmp.next
                del tmp
                tmp = cur.next
            cur = cur.next
        return head
