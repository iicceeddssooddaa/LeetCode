# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        sto = [head.val]
        temp = head
        while temp.next:
            temp = temp.next
            sto.append(temp.val)
        sto.sort()
        val = sto[0]
        head = ListNode(val)
        temp = head
        for i in range(1, len(sto) - 1):
            cache = ListNode(sto[i])
            temp.next = cache
            temp = temp.next
        if len(sto)!= 1:
            cache = ListNode(sto[-1])
            temp.next = cache
            cache.next = None
        else: head.next = None
        return head
