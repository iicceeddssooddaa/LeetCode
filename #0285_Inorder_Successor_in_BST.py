# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def inOrderTraversal(node):
            cache = []
            if node.left: cache.extend(inOrderTraversal(node.left))
            cache.append(node)
            if node.right: cache.extend(inOrderTraversal(node.right))
            return cache
        sto = inOrderTraversal(root)
        for i in range(len(sto)):
            if sto[i] == p:
                if i < len(sto) - 1: return sto[i + 1]
                else: return None
