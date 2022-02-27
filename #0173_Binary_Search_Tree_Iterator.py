# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def inOrderTraversal(node):
            cache = []
            if node.left: cache.extend(inOrderTraversal(node.left))
            cache.append(node.val)
            if node.right: cache.extend(inOrderTraversal(node.right))
            return cache
        self.record = inOrderTraversal(root)
        self.pointer = 0

    def next(self):
        """
        :rtype: int
        """
        self.pointer += 1
        return self.record[self.pointer - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer < len(self.record)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
