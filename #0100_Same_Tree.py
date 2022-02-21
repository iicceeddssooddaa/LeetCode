# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if bool(p) ^ bool(q): return False
        elif not p: return True
        elif p.val != q.val: return False
        if bool(p.left) ^ bool(q.left): return False
        elif not self.isSameTree(p.left, q.left): return False
        if bool(p.right) ^ bool(q.right): return False
        elif not self.isSameTree(p.right, q.right): return False
        return True
