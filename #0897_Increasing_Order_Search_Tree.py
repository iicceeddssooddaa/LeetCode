# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # in-order visit
        def inOrderVisit(node):
            cache = []
            if not node: return cache
            if node.left: cache.extend(inOrderVisit(node.left))
            cache.append(node.val)
            if node.right: cache.extend(inOrderVisit(node.right))
            return cache
        sto = deque(inOrderVisit(root))
        new_root = TreeNode(sto.popleft())
        temp = new_root
        while len(sto) != 0:
            new_node = TreeNode(sto.popleft())
            temp.right = new_node
            temp = temp.right
        return new_root
