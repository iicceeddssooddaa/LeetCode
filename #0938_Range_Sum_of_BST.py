# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sto = 0
        if root.left: sto += self.rangeSumBST(root.left, low, high)
        if root.right: sto += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high: sto += root.val
        return sto
