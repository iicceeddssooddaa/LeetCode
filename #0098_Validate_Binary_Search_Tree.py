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
