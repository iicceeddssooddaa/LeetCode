# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        sto, temp = [head.val], head
        while temp.next:
            temp = temp.next
            sto.append(temp.val)
        return sto == sto[-1::-1]
