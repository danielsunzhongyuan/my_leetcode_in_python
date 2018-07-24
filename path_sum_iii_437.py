# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        self.helper(root, 0, sum, res)
        return res[0] + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def helper(self, node, current_sum, sum, res):
        if not node:
            return 
        current_sum += node.val
        if current_sum == sum:
            res[0] += 1
        self.helper(node.left, current_sum, sum, res)
        self.helper(node.right, current_sum, sum, res)
        
