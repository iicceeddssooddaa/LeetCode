# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s) == 0: return None
        i, diff, n = 0, 0, len(s)
        while i < n and s[i] != "(": i += 1
        if i == n: 
            x = int(s)
            root = TreeNode(x)
            return root
        x = int(s[:i])
        diff = 1
        root, j = TreeNode(x), i + 1
        while j < n and diff !=0: 
            if s[j] == "(": diff += 1
            if s[j] == ")": diff -= 1
            j += 1
        root.left = self.str2tree(s[i + 1:j - 1])
        if j < n: root.right = self.str2tree(s[j + 1: -1])
        return root
