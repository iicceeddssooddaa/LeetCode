# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 由于是第二小，因而必然是某节点左右子节点之一（如存在），每个点传回两个值即可：最小和目前为止第二小。遍历子树而后汇总。
        if not root: return -1
        def twoMinima(node):
            if node.left:
                a1, b1 = twoMinima(node.left)
                a2, b2 = twoMinima(node.right)
                cache = set([a1, a2, b1, b2])
                if len(cache) != 1: 
                    cache_set = sorted(cache)
                    return cache_set[0], cache_set[1]
                return a1, a1
            else: return node.val, node.val
        a, b = twoMinima(root)
        if a == b: return -1
        return b
