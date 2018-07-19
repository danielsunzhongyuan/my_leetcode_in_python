# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         ret = []
#         self.inorderTraversalRecursion(root, ret)
#         return ret
        
#     def inorderTraversalRecursion(self, root, arr):
#         if root == None:
#             return
#         self.inorderTraversalRecursion(root.left, arr)
#         arr.append(root.val)
#         self.inorderTraversalRecursion(root.right, arr)
    def inorderTraversal(self, root):
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right
        return res
