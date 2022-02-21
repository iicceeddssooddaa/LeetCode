# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        _set, found = set(), False
        
        def targetList(root, k, cache_set):
            if root.val not in cache_set: cache_set.add(k - root.val)
            else: return cache_set, True
            if root.left: 
                a, b = targetList(root.left, k, cache_set)
                if b == True: return cache_set, True
                else: cache_set.union(a)
            if root.right: 
                a, b = targetList(root.right, k, cache_set)
                if b == True: return cache_set, True
                else: cache_set.union(a)
            return cache_set, False
        a, b = targetList(root, k, _set)    
        if b == True: return True
        else: return False
-------
# 多返回值成功，一次试验
