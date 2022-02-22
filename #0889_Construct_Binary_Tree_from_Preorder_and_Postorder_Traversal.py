# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            cache = preorder[1]
            for i in range(0, len(preorder) - 1):
                if postorder[i] == cache: break
            root.left = self.constructFromPrePost(preorder[1:i + 2], postorder[:i + 1])
            if i + 2 < len(preorder):
                root.right = self.constructFromPrePost(preorder[i + 2:], postorder[i + 1: -1])
        return root
