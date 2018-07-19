# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if not root:
        #     return None
        # runner = root
        # while runner.val != val:
        #     if runner.val < val:
        #         if runner.right:
        #             runner = runner.right
        #         else:
        #             return None
        #     elif runner.val > val:
        #         if runner.left:
        #             runner = runner.left
        #         else:
        #             return None
        #     else:
        #         return runner
        # return runner
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
