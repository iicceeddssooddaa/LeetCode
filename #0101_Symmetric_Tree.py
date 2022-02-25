# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preOrderTraversal(node):
            cache = []
            cache.append(node.val)
            if not node.left and not node.right: return cache
            if node.left: cache.extend(preOrderTraversal(node.left))
            else: cache.append("n")
            if node.right: cache.extend(preOrderTraversal(node.right))
            else: cache.append("n")
            return cache
        def postOrderTraversal(node):
            cache = []
            if not node.left and not node.right: return [node.val]
            if node.left: cache.extend(postOrderTraversal(node.left))
            else: cache.append("n")
            if node.right: cache.extend(postOrderTraversal(node.right))
            else: cache.append("n")
            cache.append(node.val)
            return cache
        pre, post = preOrderTraversal(root), postOrderTraversal(root)
        return pre == post[-1::-1]
