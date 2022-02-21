# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            if root1.left and root2.left: root.left = self.mergeTrees(root1.left, root2.left)
            elif root1.left: root.left = root1.left
            elif root2.left: root.left = root2.left
            if root1.right and root2.right: root.right = self.mergeTrees(root1.right, root2.right)
            elif root1.right: root.right = root1.right
            elif root2.right: root.right = root2.right
        elif root1: root = root1
        elif root2: root = root2
        else: return None
        return root
