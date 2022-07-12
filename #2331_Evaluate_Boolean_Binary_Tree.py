class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val < 2: return bool(root.val)
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else: return self.evaluateTree(root.left) and self.evaluateTree(root.right)
