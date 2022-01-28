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
        num1, num2 = l1.val, l2.val
        cur1 = l1.next
        cur2 = l2.next
        while cur1:
            num1 *= 10
            num1 += cur1.val
            cur1 = cur1.next
        while cur2:
            num2 *= 10
            num2 += cur2.val
            cur2 = cur2.next
        num = num1 + num2
        head = ListNode(num%10, None)
        num //= 10
        while num > 0:
            node = ListNode(num%10, None)
            num //= 10
            node.next = head
            head = node
        return head
      #速度不太好，存储凑合
