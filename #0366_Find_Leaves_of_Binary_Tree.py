# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def maxLevelFromLeaf(node):
            if not node.left and not node.right: return [[0, node.val]], 0
            alist, level_left, level_right = [], 0, 0
            if node.left: 
                left, level_left = maxLevelFromLeaf(node.left)
                alist.extend(left)
            if node.right: 
                right, level_right = maxLevelFromLeaf(node.right)
                alist.extend(right)
            newlevel = max(level_left, level_right) + 1
            alist.append([newlevel, node.val])
            return alist, newlevel
        sto, level= maxLevelFromLeaf(root)
        result = []
        sto.sort()
        for i in range(len(sto)):
            if sto[i][0] < len(result): result[-1].append(sto[i][1])
            else: result.append([sto[i][1]])
        return result
