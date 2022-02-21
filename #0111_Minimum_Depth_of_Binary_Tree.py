# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.left:
            left_dep = self.minDepth(root.left)
            if root.right:
                right_dep = self.minDepth(root.right)
                dep = min(left_dep, right_dep) + 1
            else: dep = left_dep + 1
        elif root.right: dep = self.minDepth(root.right) + 1
        else: dep = 1
        return dep
