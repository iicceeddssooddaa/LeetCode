"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        nodelist = []
        for child in root.children: nodelist.extend(self.postorder(child))
        nodelist.append(root.val)
        return nodelist
