# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        node_list, temp = [head], head
        while temp.next:
            temp = temp.next
            node_list.append(temp)
        if len(node_list) < 3: return head
        i, j = 0, 1
        while i < len(node_list) - 2:
            node_list[i].next = node_list[i + 2]
            i += 2
        node_list[i].next = node_list[j]
        while j < len(node_list) - 2:
            node_list[j].next = node_list[j + 2]
            j += 2
        node_list[j].next = None
        return head
----------------------
# 空间复杂度不合格  
----------------------
