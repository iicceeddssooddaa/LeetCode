# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        _dict = {}
        if not root: return False
        def idDict(root, myDict, level):
            level += 1
            if root.left:
                myDict[root.left.val] = [root, root.left, level]
                # myDict[root.left.val] = [root, level]
                idDict(root.left, myDict, level)
            if root.right:
                myDict[root.right.val] = [root, root.right, level]
                # myDict[root.right.val] = [root, level]
                idDict(root.right, myDict, level)
        idDict(root, _dict, 0)
        if x in _dict and y in _dict:
            return _dict[x][2] == _dict[y][2] and _dict[x][0] != _dict[y][0]
        return False
