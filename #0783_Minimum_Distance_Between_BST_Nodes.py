# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 由于BST，因而中序遍历为单调序列。因此逐步中序遍历记录相邻差。
        def inOrderTraversal(node):
            if not node.left and not node.right: return [node]
            cache = []
            if node.left: cache.extend(inOrderTraversal(node.left))
            cache.append(node)
            if node.right: cache.extend(inOrderTraversal(node.right))
            return cache
        queue, temp = deque(inOrderTraversal(root)), float("inf")
        node1 = queue.popleft()
        for i in range(len(queue)):
            node2 = queue.popleft()
            temp = min(temp, node2.val - node1.val)
            node1 = node2
        return temp
