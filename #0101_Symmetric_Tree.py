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
----------------------
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
        def areSymmetric(node1, node2):
            if node1.val != node2.val: return False
            if node1.left and not node2.right: return False
            if not node1.left and node2.right: return False
            if not node1.left and not node2.right: pass
            else: 
                if not areSymmetric(node1.left, node2.right): return False
            if node1.right and not node2.left: return False
            if not node1.right and node2.left: return False
            if not node1.right and not node2.left: pass
            else: 
                if not areSymmetric(node1.right, node2.left): return False
            return True
        if not root.left and not root.right: return True
        if not root.left and root.right: return False
        if root.left and not root.right: return False
        return areSymmetric(root.left, root.right)
