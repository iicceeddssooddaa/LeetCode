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
        temp, sto = head, [head]
        while temp.next:
            temp = temp.next
            sto.append(temp)
        sto.reverse()
        newhead = sto[0]
        temp = newhead
        sto[-1].next = None
        for i in range(1, len(sto)):
            temp.next = sto[i]
            temp = temp.next
        return newhead
