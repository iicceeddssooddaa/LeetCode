# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodelist = []
        def hasLonelyNode(node1, node2):
            if node1.left == node2 and not node1.right: return True
            if node1.right == node2 and not node1.left: return True
            return False
        if root.left:
            if hasLonelyNode(root, root.left): nodelist.append(root.left.val)
            nodelist.extend(self.getLonelyNodes(root.left))
        if root.right:
            if hasLonelyNode(root, root.right): nodelist.append(root.right.val)
            nodelist.extend(self.getLonelyNodes(root.right))
        return nodelist
