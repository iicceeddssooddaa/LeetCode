# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        def pathSum(node, prefix):
            if not node.left and not node.right: return [prefix]
            cache = []
            if node.left: cache.extend(pathSum(node.left, prefix + node.left.val))
            if node.right: cache.extend(pathSum(node.right, prefix + node.right.val))
            return cache
        sto = pathSum(root, root.val)
        return targetSum in sto
------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        def pathSum(node, prefix, targetSum):
            if not node.left and not node.right: return prefix == targetSum
            left, right = False, False
            if node.left: left = pathSum(node.left, prefix + node.left.val, targetSum)
            if node.right: right = pathSum(node.right, prefix + node.right.val, targetSum)
            return left or right
        return pathSum(root, root.val, targetSum)
#     以为只传真值快一点，没想到更慢了
