"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue, sto = deque([[root,0]]), []
        if not root: return []
        while len(queue) != 0:
            cur, level = queue.popleft()
            if cur.children: 
                for child in cur.children:
                    queue.append([child, level + 1])
            if len(sto) == level: sto.append([cur.val])
            else: sto[-1].append(cur.val)
        return sto
