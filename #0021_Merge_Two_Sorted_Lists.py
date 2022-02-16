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
-----------------------
# 时隔数日再写，结构完整了不少
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
        if not list1: return list2
        if not list2: return list1
        temp1, temp2, head1, head2 = list1, list2, list1, list2
        temp = ListNode(0)
        head = temp
        while head1 and head2:
            if head1.val < head2.val:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next
        if head1: temp.next = head1
        if head2: temp.next = head2
        return head.next
