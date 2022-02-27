# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_list, temp = [head], head
        while temp.next:
            temp = temp.next
            node_list.append(temp)
        if len(node_list) == 1 and n == 1: return None
        elif n == 1: node_list[-2].next = None
        elif n == len(node_list): head = node_list[1]
        else: node_list[-1 * n - 1].next = node_list[-1 * n + 1]
        return head
