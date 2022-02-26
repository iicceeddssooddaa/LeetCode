# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        temp, sto = head, [head.val]
        while temp.next:
            temp = temp.next
            sto.append(temp.val)
        sto.reverse()
        newhead = ListNode(sto[0])
        temp = newhead
        for i in range(1, len(sto)):
            cache = ListNode(sto[i])
            temp.next = cache
            temp = temp.next
        return newhead
