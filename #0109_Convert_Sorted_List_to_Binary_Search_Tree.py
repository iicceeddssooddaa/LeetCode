# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: return None
        temp, sto = head, [head.val]
        while temp.next:
            temp = temp.next
            sto.append(temp.val)
        
        def sortedArrayToBST(nums):
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            if len(nums[:mid]) != 0: root.left = sortedArrayToBST(nums[:mid])
            if len(nums[mid + 1:]) != 0: root.right = sortedArrayToBST(nums[mid + 1:])
            return root
        
        return sortedArrayToBST(sto)
