# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)
        def insertLeaf(node, val):
            if val < node.val:
                if not node.left: 
                    cache = TreeNode(val)
                    node.left = cache
                else: insertLeaf(node.left, val)
            else:
                if not node.right: 
                    cache = TreeNode(val)
                    node.right = cache
                else: insertLeaf(node.right, val)
        insertLeaf(root, val)
        return root
