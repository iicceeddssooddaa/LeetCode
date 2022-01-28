# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        cur1 = l1
        cur2 = l2
        cache = (cur1.val + cur2.val) %10
        carry = (cur1.val + cur2.val) > 9
        head = ListNode(cache)
        tail = head
        cur1 = cur1.next
        cur2 = cur2.next
        while cur1 and cur2:
            cache = (cur1.val + cur2.val + carry) %10
            carry = (cur1.val + cur2.val + carry) > 9
            node = ListNode(cache)
            tail.next = node
            tail = node
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            cache = (cur1.val + carry) %10
            carry = (cur1.val + carry) > 9
            node = ListNode(cache)
            tail.next = node
            tail = node
            cur1 = cur1.next
        while cur2:
            cache = (cur2.val + carry) %10
            carry = (cur2.val + carry) > 9
            node = ListNode(cache)
            tail.next = node
            tail = node
            cur2 = cur2.next
        if carry:
            node = ListNode(1)
            tail.next = node
        return head
-----------
#更新
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        cur1 = l1
        cur2 = l2
        head = ListNode(0)
        tail = head
        carry = 0
        while cur1 and cur2:
            cache = (cur1.val + cur2.val + carry) %10
            carry = (cur1.val + cur2.val + carry) > 9
            node = ListNode(cache)
            tail.next = node
            tail = node
            cur1 = cur1.next
            cur2 = cur2.next
        cur = cur1 if cur1 else cur2
        while cur:
            cache = (cur.val + carry) %10
            carry = (cur.val + carry) > 9
            node = ListNode(cache)
            tail.next = node
            tail = node
            cur = cur.next
        if carry:
            node = ListNode(1)
            tail.next = node
        head = head.next
        return head
