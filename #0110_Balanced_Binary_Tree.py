# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def maxDepth(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root: return 0
            left_dep = maxDepth(root.left) if root.left else 0
            right_dep = maxDepth(root.right) if root.right else 0
            return max(left_dep, right_dep) + 1
        
        if root.left:
            if not self.isBalanced(root.left): return False
            elif root.right:
                if not self.isBalanced(root.right): return False
                if abs(maxDepth(root.left) - maxDepth(root.right)) > 1: return False
            elif maxDepth(root.left) > 1: return False
        elif root.right:
            if not self.isBalanced or maxDepth(root.right) > 1: return False
        return True
