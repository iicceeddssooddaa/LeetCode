# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.left:
            if not root.left.left and not root.left.right and root.left.val == target: root.left = None
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        if root.right:
            if not root.right.left and not root.right.right and root.right.val == target: root.right = None
        if not root.left and not root.right and root.val == target: return None
        return root
