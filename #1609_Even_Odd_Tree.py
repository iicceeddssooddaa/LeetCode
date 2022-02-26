# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def levelOrderTraversal(node, level, adict):
            if level in adict: adict[level].append(node.val)
            else: adict[level] = [node.val]
            if node.left: levelOrderTraversal(node.left, level + 1, adict)
            if node.right: levelOrderTraversal(node.right, level + 1, adict)
            return adict
        _dict = levelOrderTraversal(root, 0, {})
        lvl = len(_dict)
        
        def checkMon(num, alist):
            k = len(alist)
            if num %2 == 0:
                for j in range(k - 1):
                    if alist[j] %2 == 0: return False
                    if alist[j] >= alist[j + 1]: return False
                if alist[-1] %2 == 0: return False
            else:
                for j in range(k - 1):
                    if alist[j] %2 != 0: return False
                    if alist[j] <= alist[j + 1]: return False
                if alist[-1] %2 != 0: return False
            return True
            
        for i in range(lvl):
            if not checkMon(i, _dict[i]): return False
        return True
            
