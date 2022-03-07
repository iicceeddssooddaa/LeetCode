# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        nodelist = [head]
        temp = head
        while temp.next:
            temp = temp.next
            nodelist.append(temp)
        k %= len(nodelist)
        if k == 0: return head
        newhead = nodelist[-k]
        nodelist[-1].next = nodelist[0]
        nodelist[-k - 1].next = None
        return newhead
