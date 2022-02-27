# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        cache_val = temp.val
        if temp.next:
            node.val = cache_val
            cur = temp.next
            node.next = cur
        else: 
            node.val = cache_val
            node.next = None
