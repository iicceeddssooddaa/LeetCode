# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        while head.val == val and head.next: head = head.next
        if head.val == val and not head.next: return None
        if not head.next: return head
        temp = head
        while temp.next:
            rear = temp
            temp = temp.next
            while temp.val == val and temp.next: 
                temp = temp.next
                rear.next = temp
            if temp.val == val and not temp.next: rear.next = None
        return head
