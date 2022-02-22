# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def subTree(node):
            """
            rtype: int - original sum
            int - sum of tilt
            """
            if not node: return 0,0
            if node.left:
                if node.right:
                    a1, b1 = subTree(node.left)
                    a2, b2 = subTree(node.right)
                    node_sum = a1 + a2 + node.val
                    node_tilt_sum = abs(a1 - a2) + b1 + b2
                else:
                    a, b = subTree(node.left)
                    node_sum = a + node.val
                    node_tilt_sum = abs(a) + b
            elif node.right:
                a, b = subTree(node.right)
                node_sum = a + node.val
                node_tilt_sum = abs(a) + b
            else:
                node_tilt_sum = 0
                node_sum = node.val
            return node_sum, node_tilt_sum
        a, b = subTree(root)
        return b
