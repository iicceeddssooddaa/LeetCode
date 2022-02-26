# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inOrderTraversal(node):
            if not node: return []
            cache = []
            if node.left: cache.extend(inOrderTraversal(node.left))
            cache.append(node.val)
            if node.right: cache.extend(inOrderTraversal(node.right))
            return cache
        nums1 = inOrderTraversal(root1)
        nums2 = inOrderTraversal(root2)
        if not root1: return nums2
        if not root2: return nums1
        i, j, sto = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]: 
                sto.append(nums1[i])
                i += 1
            else:
                sto.append(nums2[j])
                j += 1
        if i < len(nums1): sto.extend(nums1[i:])
        if j < len(nums2): sto.extend(nums2[j:])
        return sto
---------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inOrderTraversal(node):
            if not node: return []
            cache = []
            if node.left: cache.extend(inOrderTraversal(node.left))
            cache.append(node.val)
            if node.right: cache.extend(inOrderTraversal(node.right))
            return cache
        sto = inOrderTraversal(root1)
        sto.extend(inOrderTraversal(root2))
        sto.sort()
        return sto
  ---------
  # if not root1: return inOrderTraversal(root2)
        # elif not root2: return inOrderTraversal(root1)
        # cache = []
        # if root1.val == root2.val:
        #     cache.extend(self.getAllElements(root1.left, root2.left))
        #     cache.extend([root1.val, root2.val])
        #     cache.extend(self.getAllElements(root1.right, root2.right))
        # if root1.val < root2.val:
        #     temp1, temp2 = root1.right, root2.left
        #     root1.right, root2.left = None, None
        #     cache.extend(self.getAllElements(root1, temp2))
        #     cache.extend(self.getAllElements(temp1, root2))
        # if root1.val > root2.val:
        #     temp1, temp2 = root1.left, root2.right
        #     root1.left, root2.right = None, None
        #     cache.extend(self.getAllElements(temp1, root2))
        #     cache.extend(self.getAllElements(root1, temp2))
        # return cache
#         迭代没写对
