# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue, sto = deque([[root,0]]), []
        if not root: return []
        while len(queue) != 0:
            cur, level = queue.popleft()
            if cur.left: queue.append([cur.left, level + 1])
            if cur.right: queue.append([cur.right, level + 1])
            if len(sto) == level: sto.insert(0,[cur.val])
            else: sto[0].append(cur.val)
        return sto
