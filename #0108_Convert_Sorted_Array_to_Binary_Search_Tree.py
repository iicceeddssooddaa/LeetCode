# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        mid = len(nums)//2
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        root = TreeNode(nums[mid])
        if len(nums[:mid]) != 0: root.left = self.sortedArrayToBST(nums[:mid])
        if len(nums[mid + 1:]) != 0: root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
