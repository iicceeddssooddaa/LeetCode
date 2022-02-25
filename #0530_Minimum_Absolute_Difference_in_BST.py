# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def record(node):
            cache = []
            if node.right: cache.extend(record(node.right))
            cache.append(node.val)
            if node.left: cache.extend(record(node.left))
            return cache
        sto, curmin = record(root), float("inf")
        print sto
        for i in range(len(sto) - 1):
            curmin = min(curmin, sto[i] - sto[i + 1])
        return curmin
