# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def potGain(node):
            """
            rtype: int if node not robbed
            rtype: int if node robbed
            """
            if not node.left and not node.right: return 0, node.val
            if node.left:
                if node.right:
                    a1, b1 = potGain(node.left)
                    a2, b2 = potGain(node.right)
                    return max(a1 + a2, a1 + b2, b1 + a2, b1 + b2), a1 + a2 + node.val
                else:
                    a, b = potGain(node.left)
                    return max(a, b), a + node.val
            if node.right:
                a, b = potGain(node.right)
                return max(a, b), a + node.val
        a, b = potGain(root)
        return max(a,b)
