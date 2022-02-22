# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue, sto, avg = deque([[root,0]]), [], []
        if not root: return []
        while len(queue) != 0:
            cur, level = queue.popleft()
            if cur.left: queue.append([cur.left, level + 1])
            if cur.right: queue.append([cur.right, level + 1])
            if len(sto) == level: sto.append([cur.val])
            else: sto[-1].append(cur.val)
        for record in sto:
            avg.append(float(sum(record))/float(len(record)))
        return avg
