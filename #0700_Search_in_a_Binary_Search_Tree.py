# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val: return root
        if root.left:
            cache = self.searchBST(root.left, val)
            if cache: return cache
        if root.right:
            cache = self.searchBST(root.right, val)
            if cache: return cache
        return None
