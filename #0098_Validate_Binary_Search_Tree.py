class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        val = []
        
        def inOrderTraversal(node, li):
            if node.left:
                temp = []
                li.extend(inOrderTraversal(node.left, temp))
            li.append(node.val)
            if node.right:
                temp = []
                li.extend(inOrderTraversal(node.right, temp))
            return li
        
        val = inOrderTraversal(root, val)
        
        n, curr = len(val), val[0]
        for i in range(1, n):
            if curr < val[i]: curr = val[i]
            else: return False
        return True
-------
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def min_max(node):
            if (not node.left) and (not node.right): return node.val, node.val
            temp_min, temp_max = float("inf"), float("-inf")
            if node.left:
                l_min, l_max = min_max(node.left)
                if l_max >= node.val: return float("-inf"), float("inf")
                else: temp_min, temp_max = min(temp_min, l_min), max(temp_max, node.val)
            if node.right:
                r_min, r_max = min_max(node.right)
                if r_min <= node.val: return float("-inf"), float("inf")
                else: temp_min, temp_max = min(temp_min, node.val), max(temp_max, r_max)
            return temp_min, temp_max
        
        a, b = min_max(root)
        if a > float("-inf") and b < float("inf"): return True
        else: return False
        
