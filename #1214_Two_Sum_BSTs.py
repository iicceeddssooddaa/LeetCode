# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        _set = set()
        
        def storage(node, target, cache_set):
            if not node: return cache_set
            cache_set.add(target - node.val)
            if node.left: cache_set.union(storage(node.left, target, cache_set))
            if node.right: cache_set.union(storage(node.right, target, cache_set))
            return cache_set
        _set.union(storage(root1, target, _set))
        
        def search(node, cache_set):
            if not node: return False
            if node.val in cache_set: return True
            if node.left: 
                if search(node.left, cache_set): return True
            if node.right: 
                if search(node.right, cache_set): return True
            return False
        return search(root2, _set)
