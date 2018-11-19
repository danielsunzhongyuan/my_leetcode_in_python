# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     ret = []
    #     self.postorderTraversalRecursion(root, ret)
    #     return ret
    #
    # def postorderTraversalRecursion(self, node, arr):
    #     if node == None:
    #         return
    #     self.postorderTraversalRecursion(node.left, arr)
    #     self.postorderTraversalRecursion(node.right, arr)
    #     arr.append(node.val)
    def postorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res[::-1]
