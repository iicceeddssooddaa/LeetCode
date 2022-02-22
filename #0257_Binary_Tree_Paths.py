# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return [""]
        if not root.left and not root.right: return [str(root.val)]
        sto = []
        if root.left:
            left = self.binaryTreePaths(root.left)
            for path in left:
                cache = []
                cache[:] = path
                prefix = [str(root.val), "->"]
                prefix.extend(cache)
                string = "".join(prefix)
                sto.append(string)
        if root.right:
            right = self.binaryTreePaths(root.right)
            for path in right:
                cache = []
                cache[:] = path
                prefix = [str(root.val), "->"]
                prefix.extend(cache)
                string = "".join(prefix)
                sto.append(string)
        return sto
