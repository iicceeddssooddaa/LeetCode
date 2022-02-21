# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        if root.left:
            if root.right: root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            else: root.left, root.right = None, self.invertTree(root.left)
        else: root.left, root.right = self.invertTree(root.right), None
        return root
