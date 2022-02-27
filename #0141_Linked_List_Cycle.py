# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        head.val, temp = 10**5 + 1, head
        while temp.next:
            temp = temp.next
            if temp.val == 10**5 + 1: return True
            else: temp.val = 10**5 + 1
        return False
