# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not head: return [None for _ in range(k)]
        nodelist, temp, result = [head], head, [None for _ in range(k)]
        while temp.next:
            temp = temp.next
            nodelist.append(temp)
        # print nodelist
        if k >= len(nodelist):
            for i in range(len(nodelist)):
                result[i] = nodelist[i]
                nodelist[i].next = None
            return result
        a, b = len(nodelist) // k, len(nodelist) %k
        result[0], j = head, 0
        if b !=0: j += a + 1
        for i in range(1, b):
            result[i] = nodelist[j]
            nodelist[j - 1].next = None
            j += (a + 1)
        for i in range(b, k):
            result[i] = nodelist[j]
            nodelist[j - 1].next = None
            j += a
        return result
