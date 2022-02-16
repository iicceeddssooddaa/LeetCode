# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        if head.next:
            result = head.next
            temp = ListNode(0)
            temp.next = head
        else: return head
        front = head
        while front.next:
            rear = front.next
            if rear.next:
                cache = rear.next
                front.next = cache
                rear.next = front
                temp.next = rear
                temp = front
                front = cache
            else:
                front.next = None
                rear.next = front
                temp.next = rear
        return result
