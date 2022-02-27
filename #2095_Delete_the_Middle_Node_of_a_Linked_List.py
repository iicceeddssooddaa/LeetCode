# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count, temp = 1, head
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
        if count == 1: return None
        if count == 2: 
            head.next = None
            return head
        k = count//2
        
        i, temp = 1, head
        while i < k:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        return head
        
