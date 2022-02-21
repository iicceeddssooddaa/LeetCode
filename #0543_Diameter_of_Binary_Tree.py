# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def levelDiam(node):
            if not node: return 0,0
            if node.left:
                if node.right:
                    a1, b1 = levelDiam(node.left)
                    a2, b2 = levelDiam(node.right)
                    level = max(a1, a2) + 1
                    diam = max(a1 + a2 + 2, b1, b2)
                else:
                    a, b = levelDiam(node.left)
                    level = a + 1
                    diam = max(a + 1, b)
            elif node.right:
                a, b = levelDiam(node.right)
                level = a + 1
                diam = max(a + 1, b)
            else: level, diam = 0, 0
            return level, diam
        a, b = levelDiam(root)
        return b
