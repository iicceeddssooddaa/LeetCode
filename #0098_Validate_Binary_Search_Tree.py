# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        def record(node):
            cache = []
            if node.left: cache.extend(record(node.left))
            cache.append(node.val)
            if node.right: cache.extend(record(node.right))
            return cache
        sto = record(root)
        for i in range(len(sto) - 1):
            if sto[i] >= sto[i + 1]: return False
        return True
