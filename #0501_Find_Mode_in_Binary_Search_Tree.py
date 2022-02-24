# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def record(node):
            cache = []
            if node.left: cache.extend(record(node.left))
            cache.append(node.val)
            if node.right: cache.extend(record(node.right))
            return cache
        sto = record(root)
        counter, max_count = collections.Counter(sto), 0
        for key, value in counter.items(): max_count = max(max_count, value)
        mode_list = []
        for key, value in counter.items(): 
            if value == max_count: mode_list.append(key)
        return mode_list
