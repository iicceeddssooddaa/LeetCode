# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def divNConquer(node, prefix):
            if not node.left and not node.right: return prefix
            total = 0
            if node.left: total += divNConquer(node.left, prefix * 2 + node.left.val)
            if node.right: total += divNConquer(node.right, prefix * 2 + node.right.val)
            return total
        return divNConquer(root, root.val)
