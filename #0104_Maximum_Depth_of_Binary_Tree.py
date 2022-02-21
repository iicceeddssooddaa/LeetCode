# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left_dep = self.maxDepth(root.left) if root.left else 0
        right_dep = self.maxDepth(root.right) if root.right else 0
        return max(left_dep, right_dep) + 1
