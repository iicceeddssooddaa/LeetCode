# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        if not root: return []
        _dict = {}
        def pathSum(node, prefix, path, myDict):
            if not node.left and not node.right: 
                path.append(node.val)
                if prefix not in myDict: myDict[prefix] = [path]
                else: myDict[prefix].append(path)
                return myDict
            cache = []
            if node.left: 
                path1 = copy.deepcopy(path)
                path1.append(node.val)
                cache.extend(pathSum(node.left, prefix + node.left.val, path1, myDict))
            if node.right: 
                path2 = copy.deepcopy(path)
                path2.append(node.val)
                cache.extend(pathSum(node.right, prefix + node.right.val, path2, myDict))
            return myDict
        _dict = pathSum(root, root.val, [], _dict)
        return _dict[targetSum] if targetSum in _dict else []
  ------
#   得改。感觉path在传的过程中没能规避掉左右两侧反复修改的问题。用deepcopy又跑太慢了
