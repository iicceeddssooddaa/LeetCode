class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if target == float(root.val): return root.val
        
        if target < root.val:
            if root.left:
                cache = self.closestValue(root.left, target)
                if root.val - target > abs(target - cache): return cache
                else: return root.val
            else: return root.val
        
        if target > root.val:
            if root.right:
                cache = self.closestValue(root.right, target)
                if target - root.val > abs(target - cache): return cache
                else: return root.val
            else: return root.val
