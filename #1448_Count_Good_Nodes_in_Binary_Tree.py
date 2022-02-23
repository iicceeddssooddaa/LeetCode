# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        root_max = root.val
        def countGoodNodes(node, curMax):
            """
            input type: int current new max along the path
            rtype: new count of good Nodes
            """
            count = 0
            if node.val >= curMax: count += 1
            if node.left: count += countGoodNodes(node.left, max(curMax, node.val))
            if node.right: count += countGoodNodes(node.right, max(curMax, node.val))
            return count
        root_count = countGoodNodes(root, root_max)
        return root_count
