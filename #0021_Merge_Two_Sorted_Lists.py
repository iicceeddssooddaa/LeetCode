# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        cur1, cur2 = list1, list2
        if cur1.val < cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        tail = head
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = cur1
                tail = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                tail = cur2
                cur2 = cur2.next
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        return head
